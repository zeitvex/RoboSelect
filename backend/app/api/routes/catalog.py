"""目录：目录结构、零件列表、零件详情。"""
from __future__ import annotations

from typing import Annotated, Any, Literal

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import func
from sqlmodel import select

from ...crud import posts_out
from ...models import Offer, Part, Post
from ..deps import Db, MaybeUser

router = APIRouter(tags=["catalog"])

#: 品类。顺序即展示顺序：关节电机是重点，放最前。
#: 电池 / 线束 目前**没有收录** —— 不是漏了，是没有可信来源，
#: 宁可空着也不编（见 README 的口径纪律）。
CATEGORY_LABELS = {
    "actuator": "关节电机",
    "controller_high": "上位机",
    "controller_low": "下位机",
    "structure": "机械结构",
    "imu": "IMU",
    "lidar": "激光雷达",
    "camera": "深度相机",
    "battery": "电池",
    "wiring": "线束",
    "module": "其余模块",
}

#: 还没有数据的品类：前端要显示「待补充」，不能当成 500 或空列表了事
#: 电芯规格书与线束表商品页给不了，没找到可信来源前保持为空。
EMPTY_CATEGORIES = {"battery", "wiring"}
SUBTYPE_LABELS = {
    "qdd": "准直驱 QDD", "planetary": "行星减速", "harmonic": "谐波减速",
    "direct": "直驱", "sbc": "单板计算机", "mcu": "MCU / 驱动器",
    "som": "核心模组", "servo_driver": "FOC 伺服驱动器",
    "bridge": "调试桥", "imu": "IMU", "camera": "深度相机",
    "lidar": "激光雷达", "force": "力 / 触觉", "encoder": "编码器",
    # 整机形态：先按机器人外形分，再细分腿构型
    "quadruped": "四足", "wheeled_quadruped": "四轮足", "humanoid": "人形",
    "biped": "双足", "wheeled_biped": "双轮足",
    "quadruped_inward_knee": "四足 · 内膝肘",
    "wheeled_quadruped_inward_knee": "四轮足 · 内膝肘",
}

#: 允许排序的字段 → JSON 路径。白名单，用户输入不进 SQL。
SORTABLE = {
    "featured": None, "vendor": None, "model": None, "price": None, "verified": None,
    "tau_peak": "tau_peak_Nm", "tau_rated": "tau_rated_Nm", "gear": "gear",
    "mass": "mass_kg", "speed": "speed_noload_rpm",
    "armature": "armature_kgm2", "rotor_inertia": "rotor_inertia_kgm2",
    "kt": "kt_Nm_per_A", "npu_tops": "npu_tops", "power_max": "power_max_w",
    "cuda_cores": "cuda_cores", "bits": "bits",
}


def derive(specs: dict) -> dict[str, Any]:
    """派生量在读取时算，不落库。"""
    out: dict[str, Any] = {}
    tp, tr = specs.get("tau_peak_Nm"), specs.get("tau_rated_Nm")
    m = specs.get("mass_kg")
    if tp and m:
        out["torque_density_Nm_per_kg"] = round(tp / m, 1)
    if tp and tr:
        out["peak_rated_ratio"] = round(tp / tr, 2)
    rpm = specs.get("speed_noload_rpm")
    if rpm:
        out["speed_noload_rad_s"] = round(rpm * 3.141592653589793 / 30, 2)
    if tp and rpm:
        out["peak_power_W"] = round(tp * rpm * 3.141592653589793 / 30 / 4, 0)
    od, l = specs.get("od_mm"), specs.get("l_mm")
    if od and l:
        out["envelope_cm3"] = round(3.141592653589793 * (od / 20) ** 2 * (l / 10), 0)
    j, g, arm = specs.get("rotor_inertia_kgm2"), specs.get("gear"), specs.get("armature_kgm2")
    if j and g:
        out["armature_check_kgm2"] = round(j * g * g, 10)
    if arm and j and g and j * g * g:
        out["armature_ok"] = abs(arm / (j * g * g) - 1) < 1e-6
    return out


def part_out(p: Part, viewer: bool = False) -> dict:
    return {
        "id": p.id, "category": p.category,
        "category_label": CATEGORY_LABELS.get(p.category, p.category),
        "subtype": p.subtype,
        "subtype_label": SUBTYPE_LABELS.get(p.subtype, p.subtype),
        "vendor": p.vendor, "vendor_cn": p.vendor_cn, "model": p.model,
        "title": p.title, "url": p.url, "source_tier": p.source_tier,
        "verified": p.verified, "last_checked": p.last_checked,
        "price_cny": p.price_cny, "specs": p.specs, "derived": derive(p.specs),
        "notes": p.notes, "origin": p.origin,
        # 真机照片留给数据维护者填；空则前端渲染按真实尺寸画的示意图
        "image_url": (p.specs or {}).get("image_url"),
    }


def _attach_reviews(db, items: list[dict]) -> None:
    """给一页零件挂上「最高赞评价」与评价统计（一次查询，不 N+1）。"""
    ids = [i["id"] for i in items]
    if not ids:
        return
    rows = db.exec(
        select(Post).where(Post.part_id.in_(ids), Post.kind == "review")
        .order_by(Post.score.desc(), Post.created_at.desc())).all()
    best: dict[str, Post] = {}
    agg: dict[str, list[float]] = {}
    for r in rows:
        if r.part_id is None:
            continue
        best.setdefault(r.part_id, r)          # 已按 score desc 排序，第一条即最高赞
        if r.rating:
            agg.setdefault(r.part_id, []).append(float(r.rating))

    authors = {}
    author_ids = {r.author_id for r in best.values()}
    if author_ids:
        from ...models import User
        for u in db.exec(select(User).where(User.id.in_(author_ids))).all():
            authors[u.id] = {"handle": u.handle, "display_name": u.display_name,
                             "avatar_hue": u.avatar_hue, "reputation": u.reputation}

    for it in items:
        pid = it["id"]
        r = best.get(pid)
        it["review_count"] = len(agg.get(pid, [])) and len([x for x in rows if x.part_id == pid])
        ratings = agg.get(pid) or []
        it["rating_avg"] = round(sum(ratings) / len(ratings), 2) if ratings else None
        it["top_review"] = None if r is None else {
            "id": r.id, "title": r.title,
            "excerpt": (r.body or "").replace("\n", " ")[:160],
            "score": r.score, "rating": r.rating,
            "own_hardware": r.own_hardware,
            "author": authors.get(r.author_id),
        }


@router.get("/catalog")
def catalog(db: Db, category: str | None = None):
    """分类、子类、厂商。厂商按 category 收窄，避免关节电机页混进传感器厂。"""
    facets = db.exec(
        select(Part.category, Part.subtype, func.count(Part.id))
        .group_by(Part.category, Part.subtype)).all()
    rows = [{"category": c, "category_label": CATEGORY_LABELS.get(c, c),
             "subtype": s, "subtype_label": SUBTYPE_LABELS.get(s, s), "n": int(n)}
            for c, s, n in facets]
    if category:
        vendors = db.exec(select(Part.vendor, func.count(Part.id))
                          .where(Part.category == category)
                          .group_by(Part.vendor)
                          .order_by(func.count(Part.id).desc())).all()
        total = db.exec(select(func.count(Part.id))
                        .where(Part.category == category)).one()
    else:
        vendors = db.exec(select(Part.vendor, func.count(Part.id))
                          .group_by(Part.vendor)
                          .order_by(func.count(Part.id).desc())).all()
        total = db.exec(select(func.count(Part.id))).one()
    return {"total": int(total), "category": category,
            "categories": CATEGORY_LABELS, "subtypes": SUBTYPE_LABELS,
            "empty_categories": sorted(EMPTY_CATEGORIES),
            "facets": rows,
            "vendors": [{"vendor": v, "n": int(n)} for v, n in vendors],
            "sortable": list(SORTABLE)}


@router.get("/parts")
def list_parts(
    db: Db,
    category: str | None = None,
    subtype: str | None = None,
    vendor: str | None = None,
    q: str | None = None,
    source_tier: str | None = None,
    verified: bool | None = None,
    has_armature: bool | None = None,
    in_stock: bool | None = None,
    sort: str = "featured",
    order: Literal["asc", "desc"] = "asc",
    limit: Annotated[int, Query(ge=1, le=200)] = 60,
    offset: Annotated[int, Query(ge=0)] = 0,
):
    stmt = select(Part)
    if category:
        stmt = stmt.where(Part.category == category)
    if subtype:
        stmt = stmt.where(Part.subtype == subtype)
    if vendor:
        stmt = stmt.where(Part.vendor == vendor)
    if source_tier:
        stmt = stmt.where(Part.source_tier == source_tier)
    if verified is not None:
        stmt = stmt.where(Part.verified == verified)
    if q:
        stmt = stmt.where(Part.search.contains(q.lower()))
    if has_armature:
        stmt = stmt.where(func.json_extract(Part.specs, "$.armature_kgm2").isnot(None))
    if in_stock:
        stmt = stmt.where(Part.price_cny.isnot(None))

    total = db.exec(select(func.count()).select_from(stmt.subquery())).one()

    key = sort if sort in SORTABLE else "vendor"
    if key == "featured":
        # 首页默认口径：有评价的排前面（按最高赞评价的分数），其余按厂商
        best = (select(func.max(Post.score))
                .where(Post.part_id == Part.id, Post.kind == "review")
                .correlate(Part).scalar_subquery())
        stmt = stmt.order_by(best.is_(None), best.desc(), Part.vendor, Part.model)
    elif SORTABLE.get(key) is None:
        col = getattr(Part, key)
        stmt = stmt.order_by(col.is_(None), col.desc() if order == "desc" else col.asc(),
                             Part.vendor, Part.model)
    else:
        col = func.json_extract(Part.specs, f"$.{SORTABLE[key]}")
        # NULL 永远排最后，两个方向一致
        stmt = stmt.order_by(col.is_(None), col.desc() if order == "desc" else col.asc(),
                             Part.vendor, Part.model)
    stmt = stmt.offset(offset).limit(limit)

    items = [part_out(p) for p in db.exec(stmt).all()]
    _attach_reviews(db, items)
    return {"total": int(total), "limit": limit, "offset": offset,
            "sort": key, "order": order, "items": items}


@router.get("/parts/{part_id}")
def get_part(part_id: str, db: Db, user: MaybeUser):
    p = db.get(Part, part_id)
    if p is None:
        raise HTTPException(404, "零件不存在")
    offers = db.exec(select(Offer).where((Offer.part_id == part_id)
                                         | (Offer.part_id.is_(None)))).all()
    posts = db.exec(select(Post).where(Post.part_id == part_id)
                    .order_by(Post.pinned.desc(), Post.created_at.desc()).limit(50)).all()
    out = part_out(p)
    out["offers"] = [{"id": o.id, "kind": o.kind, "title": o.title,
                      "detail": o.detail, "url": o.url, "vendor": o.vendor,
                      "expires_on": o.expires_on, "demo": o.demo} for o in offers]
    out["posts"] = [x.model_dump() for x in
                    posts_out(db, list(posts), user.id if user else None)]
    return out


@router.get("/stats")
def stats(db: Db):
    n = int(db.exec(select(func.count(Part.id))).one())
    arm = int(db.exec(select(func.count(Part.id)).where(
        func.json_extract(Part.specs, "$.armature_kgm2").isnot(None))).one())
    rated = int(db.exec(select(func.count(Part.id)).where(
        func.json_extract(Part.specs, "$.tau_rated_Nm").isnot(None))).one())
    priced = int(db.exec(select(func.count(Part.id)).where(
        Part.price_cny.isnot(None))).one())
    from ...models import Comment, User
    return {
        "parts": n, "with_armature": arm, "with_rated_torque": rated,
        "with_price": priced,
        "armature_coverage": round(arm / n, 3) if n else 0,
        "users": int(db.exec(select(func.count(User.id))).one()),
        "posts": int(db.exec(select(func.count(Post.id))).one()),
        "comments": int(db.exec(select(func.count(Comment.id))).one()),
    }
