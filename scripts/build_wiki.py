"""从 data/*.json 生成 VitePress 文档站内容。

为什么生成而不是手写：目录每天在变（现在 191 个零件、14 家厂商），
手写的表格第二天就过期。这一层只做「把已核过的数据换个形态呈现」，
不引入任何新数字 —— 每个数在 SPA 里能查到的，这里也一样。

产物：
  wiki/docs/**/*.md              页面
  wiki/docs/.vitepress/sidebar.json  侧边栏（配置直接 import）
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import re
import shutil
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "wiki" / "docs"

#: 品类。顺序即展示顺序 —— 关节电机是重点，放最前。
#: 电池 / 线束 没有收录：不是漏了，是没有可信来源，宁缺不编。
CATS = [
    ("actuator", "关节电机", "选型主战场"),
    ("controller_high", "上位机", "推理与感知"),
    ("controller_low", "下位机", "力矩闭环"),
    ("structure", "机械结构", "按整机形态分类"),
    ("imu", "IMU", "姿态与振动"),
    ("lidar", "激光雷达", "地形与建图"),
    ("camera", "深度相机", "视觉感知"),
    ("battery", "电池", "待收录"),
    ("wiring", "线束", "待收录"),
    ("module", "其余模块", "力触觉 / 编码器"),
]

CAT_CN = {c: n for c, n, _ in CATS}
CAT_LABEL = CAT_CN

#: 机械结构按整机形态分类。顺序即展示顺序；没收录的子类也保留，
#: 目录页写明「待收录」，让读者知道这一类存在，而不是以为漏了。
STRUCTURE_SUBTYPES = [
    ("quadruped", "四足", "四足步态，机器狗的主流形态"),
    ("wheeled_quadruped", "四轮足", "四足加轮端驱动，轮步复合"),
    ("humanoid", "人形", "双足人形，带双臂"),
    ("biped", "双足", "不带双臂或上肢简化的双足平台"),
    ("wheeled_biped", "双轮足", "双足加轮端驱动"),
    ("quadruped_inward_knee", "四足 · 内膝肘", "前肘后膝式腿构型"),
    ("wheeled_quadruped_inward_knee", "四轮足 · 内膝肘", "前肘后膝式轮足平台"),
]
STRUCTURE_LABEL = {k: v for k, v, _ in STRUCTURE_SUBTYPES}


def slug(s: str) -> str:
    a = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    if len(a) < 2:
        a = "v" + hashlib.sha1(s.encode()).hexdigest()[:6]
    return a


def part_slug(part_id: str, vendor: str, model: str, seen: dict[str, str]) -> str:
    """型号页的 URL 片段。

    目录里的 id 含中文（`达妙-dm-dm-j4340-2ec-v1-1`），放进 URL 会被百分号编码成一串
    `%E8%BE%BE...`，分享出去很难看。所以用 厂商+型号 的 ASCII 形式，
    重名时补 6 位哈希 —— 保证唯一，且人眼看着认得。
    """
    base = re.sub(r"[^A-Za-z0-9]+", "-", f"{vendor}-{model}").strip("-").lower()
    base = re.sub(r"-+", "-", base)[:60] or "part"
    if base in seen and seen[base] != part_id:
        base = f"{base}-{hashlib.sha1(part_id.encode()).hexdigest()[:6]}"
    seen[base] = part_id
    return base



def num(v, digits: int = 3) -> str:
    if v is None or v == "":
        return "—"
    if isinstance(v, str):
        return v
    a = abs(float(v))
    if a and (a < 0.01 or a >= 100000):
        return f"{v:.2e}"
    return f"{round(float(v), digits):g}"


def load() -> list[dict]:
    """读目录数据。

    统一走 scripts/load_catalog.py：优先 data/catalog/<品类>/<厂商>.json（人工维护），
    没有才退回 data/motors.json（采集产物）。这样贡献者只改自己的那个文件，
    采集脚本重跑也不会覆盖人工修订。
    """
    from load_catalog import load_parts

    return load_parts()


def tier_badge(t: str, verified) -> str:
    mark = "✓" if verified else ""
    return f"`{t}{mark}`"



#: id -> 型号页地址。main() 里填；表格渲染时用它把型号变成可点的链接。
HREF: dict[str, str] = {}


def mdl(p: dict) -> str:
    """型号单元格：有页面就链接，没有就纯文本。"""
    href = HREF.get(p["id"])
    return f"[**{p['model']}**]({href})" if href else f"**{p['model']}**"

def actuator_table(items: list[dict]) -> str:
    head = ("| 型号 | 峰值 τ N·m | 额定 τ N·m | 减速比 | 空载 rpm | 质量 kg "
            "| 转子惯量 kg·m² | 价格 ¥ | 来源 |\n"
            "|---|---|---|---|---|---|---|---|---|")
    lines = [head]
    for p in sorted(items, key=lambda r: -(r["specs"].get("tau_peak_Nm") or 0)):
        s = p["specs"]
        lines.append(
            f"| {mdl(p)} | {num(s.get('tau_peak_Nm'))} | {num(s.get('tau_rated_Nm'))} "
            f"| {num(s.get('gear'))} | {num(s.get('speed_noload_rpm'))} | {num(s.get('mass_kg'))} "
            f"| {num(s.get('armature_kgm2'))} | "
            f"{'—' if p.get('price_cny') is None else format(int(p['price_cny']), ',')} "
            f"| {tier_badge(p['source_tier'], p['verified'])} |")
    return "\n".join(lines)


def generic_table(items: list[dict], cat: str) -> str:
    if cat == "controller_high":
        head = "| 型号 | SoC | CUDA | NPU TOPS | 内存 GB | 峰值 W | 价格 ¥ | 来源 |\n|---|---|---|---|---|---|---|---|"
        def row(p):
            s = p["specs"]
            return (f"| {mdl(p)} | {s.get('soc') or '—'} | {s.get('cuda_cores') or '—'} "
                    f"| {num(s.get('npu_tops'))} | {num(s.get('ram_gb'))} | {num(s.get('power_max_w'))} "
                    f"| {'—' if p.get('price_cny') is None else format(int(p['price_cny']), ',')} "
                    f"| {tier_badge(p['source_tier'], p['verified'])} |")
    elif cat == "controller_low":
        head = "| 型号 | MCU | FOC 轴数 | CAN | 电流环 kHz | 最高 V | 价格 ¥ | 来源 |\n|---|---|---|---|---|---|---|---|"
        def row(p):
            s = p["specs"]
            return (f"| {mdl(p)} | {s.get('mcu') or '—'} | {s.get('foc_axes') or '—'} "
                    f"| {(str(s.get('can') or '—')) + (' FD' if s.get('canfd') else '')} "
                    f"| {num(s.get('current_loop_khz'))} | {num(s.get('voltage_max_V'))} "
                    f"| {'—' if p.get('price_cny') is None else format(int(p['price_cny']), ',')} "
                    f"| {tier_badge(p['source_tier'], p['verified'])} |")
    elif cat == "camera":
        head = ("| 型号 | 深度量程 m | FOV | 帧率 fps | 接口 | 价格 ¥ | 来源 |\n"
                "|---|---|---|---|---|---|---|")
        def row(p):
            s = p["specs"]
            return (f"| {mdl(p)} | {s.get('depth_range_m') or '—'} | {s.get('fov') or '—'} "
                    f"| {num(s.get('fps'))} | {s.get('iface') or '—'} "
                    f"| {'—' if p.get('price_cny') is None else format(int(p['price_cny']), ',')} "
                    f"| {tier_badge(p['source_tier'], p['verified'])} |")
    elif cat == "lidar":
        head = ("| 型号 | 量程 m | FOV | 点频 kpts/s | 帧率 fps | 价格 ¥ | 来源 |\n"
                "|---|---|---|---|---|---|---|")
        def row(p):
            s = p["specs"]
            pps = s.get("points_per_s")
            return (f"| {mdl(p)} | {num(s.get('range_m'))} | {s.get('fov') or '—'} "
                    f"| {'—' if not pps else format(int(round(pps / 1000)), ',')} "
                    f"| {num(s.get('fps'))} "
                    f"| {'—' if p.get('price_cny') is None else format(int(p['price_cny']), ',')} "
                    f"| {tier_badge(p['source_tier'], p['verified'])} |")
    elif cat == "imu":
        head = ("| 型号 | 子类 | 陀螺量程 °/s | 加计量程 g | ODR Hz | 接口 | 价格 ¥ | 来源 |\n"
                "|---|---|---|---|---|---|---|---|")
        def row(p):
            s = p["specs"]
            return (f"| {mdl(p)} | {p.get('subtype_label') or p['subtype']} "
                    f"| {num(s.get('gyro_range_dps'))} | {num(s.get('accel_range_g'))} "
                    f"| {num(s.get('odr_hz'))} | {s.get('iface') or '—'} "
                    f"| {'—' if p.get('price_cny') is None else format(int(p['price_cny']), ',')} "
                    f"| {tier_badge(p['source_tier'], p['verified'])} |")
    elif cat == "structure":
        head = ("| 型号 | 形态 | 自由度 | 质量 kg | 负载 kg | 最大速度 m/s | 价格 ¥ | 来源 |\n"
                "|---|---|---|---|---|---|---|---|")
        def row(p):
            s = p["specs"]
            return (f"| {mdl(p)} | {p.get('subtype_label') or STRUCTURE_LABEL.get(p['subtype'], p['subtype'])} "
                    f"| {num(s.get('dof'))} | {num(s.get('mass_kg'))} | {num(s.get('payload_kg'))} "
                    f"| {num(s.get('speed_max_mps'))} "
                    f"| {'—' if p.get('price_cny') is None else format(int(p['price_cny']), ',')} "
                    f"| {tier_badge(p['source_tier'], p['verified'])} |")
    else:
        head = "| 型号 | 子类 | 接口 | 关键参数 | 价格 ¥ | 来源 |\n|---|---|---|---|---|---|"
        def row(p):
            s = p["specs"]
            keys = ("bits", "odr_hz", "iface")
            kv = "、".join(f"{k}={num(s[k])}" for k in keys if s.get(k))
            return (f"| {mdl(p)} | {p.get('subtype_label') or p['subtype']} "
                    f"| {s.get('iface') or '—'} | {kv or '—'} "
                    f"| {'—' if p.get('price_cny') is None else format(int(p['price_cny']), ',')} "
                    f"| {tier_badge(p['source_tier'], p['verified'])} |")
    return "\n".join([head] + [row(p) for p in sorted(items, key=lambda r: r["vendor"])])


FRONT = """---
title: {title}
---

"""


def main() -> None:
    rows = load()
    OUT.mkdir(parents=True, exist_ok=True)
    # 目录按 CATS 建（含空品类：它们的 index.md 要写「未收录」说明）
    #
    # 先清掉上一轮的产物：品类会变（sensor 拆成 imu/lidar/camera）、厂商会变
    # （外部 focus 收敛时移出 10 家），不清就会留下「已经不存在的型号页」，
    # 那些页面还能被访问到，等于把废弃数据留在线上。
    # 手写页面（explore.md）不在清理范围内。
    GENERATED = ["index.md", "semantics.md", "protocols.md", "sources.md"]
    for name in GENERATED:
        p = OUT / name
        if p.exists():
            p.unlink()
    if (OUT / "parts").exists():
        shutil.rmtree(OUT / "parts")
    for c, _, _ in CATS:
        (OUT / "parts" / c).mkdir(parents=True, exist_ok=True)

    # ── 每个型号独立一页 ─────────────────────────────────────────────
    # 为什么要铺开成 191 页：这样「AK80-9 V3 到底怎么样」才有能分享、能被搜到、
    # 能挂讨论的落点。厂商页只适合横向比，单型号的实测必须落在单型号页上。
    seen_slug: dict[str, str] = {}
    slugs: dict[str, str] = {}
    for r in rows:
        slugs[r["id"]] = part_slug(r["id"], r["vendor"], r["model"], seen_slug)

    # 表格里的型号要能点进型号页
    for r in rows:
        HREF[r["id"]] = f'/parts/{r["category"]}/{slugs[r["id"]]}'

    # ── 静态目录快照：让静态站也能做交互式检索 ────────────────────────
    # 数据本来就是静态的（data/*.json），排序 / 筛选 / 搜索都是客户端计算，
    # 浏览器做比 API 做更合适，而且静态站能深链、能被收录、不用养服务器。
    #
    # 卡片要显示的东西（评分、优惠）也在这里一次性烤进去 —— 静态站没有 API，
    # 卡片上不该为空着而再发一次请求。
    ratings: dict = {}
    _rp = ROOT / "data" / "ratings_snapshot.json"
    if _rp.exists():
        try:
            ratings = json.loads(_rp.read_text(encoding="utf-8")).get("parts") or {}
        except Exception:
            ratings = {}

    from load_catalog import load_offers

    offers: list[dict] = load_offers()

    def offer_of(r: dict) -> dict | None:
        """给一个零件找**当前最便宜且条件齐全**的优惠。

        优先级：具体 part_id 的 > 厂商级的；有明确优惠价的 > 只有折扣比例的。
        折扣比例（如教育优惠 9 折）用原价折算成有效价，卡片才能显示一个数。
        没有条件（detail）的一律不上卡片 —— 只给价不给条件比不给更糟。
        """
        today = date.today().isoformat()
        cand = [o for o in offers
                if (o.get("part_id") == r["id"])
                or (not o.get("part_id") and o.get("vendor") == r["vendor"])]
        cand = [o for o in cand
                if (o.get("expires_on") or "9999") >= today and o.get("detail")]

        def eff(o):
            if o.get("price_cny") is not None:
                return float(o["price_cny"])
            d = o.get("discount")
            if d and r.get("price_cny"):
                return round(float(r["price_cny"]) * float(d), 2)
            return None

        priced = [(eff(o), o) for o in cand]
        priced = [(p, o) for p, o in priced if p is not None]

        def pack(o, p):
            return {"title": o.get("title"), "kind": o.get("kind"), "price": p,
                    "discount": o.get("discount"), "condition": o.get("detail"),
                    "url": o.get("url"), "expires": o.get("expires_on"),
                    "source": o.get("source"), "demo": bool(o.get("demo"))}

        if not priced:
            o = cand[0] if cand else None
            return [pack(o, None)] if o else []
        # 全部列出：同一型号可能并行多条（首购特价 + RC 买二赠一），按价格升序
        return [pack(o, p) for p, o in sorted(priced, key=lambda x: x[0])]

    digest = []
    for r in rows:
        s = r.get("specs") or {}
        rt = ratings.get(r["id"]) or {}
        of = offer_of(r)
        digest.append({
            "id": r["id"], "slug": slugs[r["id"]],
            "category": r["category"], "subtype": r["subtype"],
            "subtypeLabel": r.get("subtype_label") or r["subtype"],
            "vendor": r["vendor"], "model": r["model"],
            "tier": r["source_tier"], "verified": bool(r["verified"]),
            "price": r.get("price_cny"),
            "image": s.get("image_url") or None,
            "rating": {"avg": rt.get("avg"), "count": rt.get("count") or 0},
            # 全部优惠按价格升序；卡片取第一条显示优惠价，其余在部件页列出
            "offers": of,
            "offer": (of[0] if of else None),
            "tauPeak": s.get("tau_peak_Nm"), "tauRated": s.get("tau_rated_Nm"),
            "gear": s.get("gear"), "mass": s.get("mass_kg"),
            "armature": s.get("armature_kgm2"),
            "rpm": s.get("speed_noload_rpm"), "od": s.get("od_mm"), "len": s.get("l_mm"),
            "soc": s.get("soc"), "npuTops": s.get("npu_tops"), "ramGb": s.get("ram_gb"),
            "mcu": s.get("mcu"), "can": s.get("can"), "iface": s.get("iface"),
            "bits": s.get("bits"), "odrHz": s.get("odr_hz"), "fps": s.get("fps"),
            "depthRange": s.get("depth_range_m"), "rangeM": s.get("range_m"),
            "notes": (r.get("notes") or "")[:600],
            "specs": {k: v for k, v in s.items() if v is not None},
        })
    pub = OUT / "public"
    pub.mkdir(parents=True, exist_ok=True)
    (pub / "catalog.json").write_text(
        json.dumps({"count": len(digest), "parts": digest},
                   ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")
    print(f"  静态目录 {len(digest)} 条 / {(pub / 'catalog.json').stat().st_size // 1024} KB")

    # 产品图：从 frontend/public/parts 复制到文档站的 public。
    # 两站要能各自独立部署，所以不能靠相对路径引用另一棵树。
    src_img = ROOT / "frontend" / "public" / "parts"
    dst_img = pub / "parts"
    copied = 0
    if src_img.exists():
        dst_img.mkdir(parents=True, exist_ok=True)
        for f in src_img.iterdir():
            if f.is_file() and f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"):
                target = dst_img / f.name
                if not target.exists() or target.stat().st_mtime < f.stat().st_mtime:
                    target.write_bytes(f.read_bytes())
                    copied += 1
    print(f"  产品图同步 {copied} 张（共 {len(list(dst_img.glob('*'))) if dst_img.exists() else 0} 张）")

    # 评分快照：纯静态部署（GitHub Pages）没有后端，页面读不到 /api/ratings，
    # 所以把「上次导出时」的聚合结果一起发布。页面上会标明这是快照。
    snap = ROOT / "data" / "ratings_snapshot.json"
    if snap.exists():
        (pub / "ratings.json").write_bytes(snap.read_bytes())
        try:
            n = len(json.loads(snap.read_text(encoding="utf-8")).get("parts") or {})
        except Exception:
            n = 0
        print(f"  评分快照 -> public/ratings.json（{n} 个零件有分）")
    else:
        (pub / "ratings.json").write_text(
            json.dumps({"total_ratings": 0, "parts": {}, "snapshot": True},
                       ensure_ascii=False), encoding="utf-8")
        print("  评分快照：无，写空表")

    # ── 生成 191 个型号页 ─────────────────────────────────────────────
    SPEC_LABEL = {
        "tau_peak_Nm": "峰值扭矩 (N·m)", "tau_rated_Nm": "额定扭矩 (N·m)",
        "tau_basis": "扭矩口径", "speed_noload_rpm": "空载转速 (rpm)",
        "speed_rated_rpm": "额定转速 (rpm)", "gear": "减速比",
        "mass_kg": "质量 (kg)", "od_mm": "外径 (mm)", "l_mm": "长度 (mm)",
        "rotor_inertia_kgm2": "转子惯量 (kg·m²)", "inertia_basis": "惯量口径",
        "armature_kgm2": "转子惯量 (kg·m²)", "voltage_V": "额定电压 (V)",
        "voltage_range_V": "电压范围 (V)", "kt_Nm_per_A": "转矩常数 (N·m/A)",
        "r_phase_ohm": "相电阻 (Ω)", "l_phase_uh": "相电感 (µH)",
        "pole_pairs": "极对数", "i_peak_A": "峰值电流 (A)", "i_rated_A": "额定电流 (A)",
        "encoder": "编码器", "comm": "通信", "driver_integrated": "内置驱动",
        "ip": "防护等级", "frictionloss_Nm": "摩擦 (N·m)",
        "damping_Nms_rad": "阻尼 (N·m·s/rad)", "soc": "SoC",
        "cuda_cores": "CUDA 核", "npu_tops": "NPU (TOPS)", "ram_gb": "内存 (GB)",
        "power_max_w": "峰值功耗 (W)", "mcu": "MCU", "can": "CAN 路数",
        "canfd": "CAN-FD", "current_loop_khz": "电流环 (kHz)",
        "voltage_max_V": "最高电压 (V)", "foc_axes": "FOC 轴数",
        "iface": "接口", "bits": "位宽 (bit)", "fps": "帧率 (fps)",
        "odr_hz": "ODR (Hz)", "range_m": "量程 (m)", "depth_range_m": "深度量程 (m)",
        "gyro_range_dps": "陀螺量程 (°/s)", "accel_range_g": "加速度量程 (g)",
        "noise": "噪声", "resolution": "分辨率", "points_per_s": "点频 (pts/s)",
        "channel": "线数 / 通道", "absolute": "精度 / 绝对式",
        "temp_range_C": "工作温度 (°C)", "power_w": "功耗 (W)", "fov": "视场角 (FOV)",
        "image_url": "产品图", "image_source": "图片来源",
        "cpu": "CPU", "cores": "核心数", "cpu_arch": "架构",
        "ram_bw_gbs": "内存带宽 (GB/s)", "storage_gb": "板载存储 (GB)",
        "power_idle_w": "待机功耗 (W)", "os": "系统", "cuda": "CUDA",
        "ros2": "ROS 2", "eth": "网口", "usb": "USB", "csi": "CSI 相机口",
        "pcie": "PCIe / M.2", "size_mm": "尺寸 (mm)", "weight_g": "重量 (g)",
        "clock_mhz": "主频 (MHz)", "ram_kb": "RAM (KB)", "flash_kb": "Flash (KB)",
        "torque_mode": "力矩模式", "voltage_in_V": "额定输入电压 (V)",
        "comm_upper": "上位机通信",
        # 整机形态
        "dof": "自由度", "payload_kg": "负载 (kg)", "speed_max_mps": "最大速度 (m/s)",
        "climb_height_mm": "攀爬落差 (mm)", "climb_angle_deg": "爬坡角度 (°)",
        "endurance_h": "续航 (h)", "battery": "电池", "compute": "算力",
        "sensors": "传感器",
    }

    def spec_rows(specs: dict, category: str = "") -> str:
        out = []
        for k, v in specs.items():
            if k in ("image_url", "image_source", "doc_url", "doc_pdf", "repo_urls", "urdf_urls"):
                continue
            label = SPEC_LABEL.get(k, k)
            if k == "points_per_s" and isinstance(v, (int, float)):
                val = format(int(v), ",")
            elif isinstance(v, bool) and category.startswith("controller"):
                val = "是" if v else "否"
            else:
                val = "—" if v is None else (str(v) if isinstance(v, str) else num(v, 4))
            out.append(f"| {label} | {val} |")
        return "\n".join(out)

    # ── 每页要用的派生量（只对关节电机算，其它品类没有这些语义）─────────
    def metrics(r: dict) -> list[tuple[str, str, str, str]]:
        """返回 (指标, 值, 判据, 级别) —— 级别 good/warn/bad/na"""
        s = r.get("specs") or {}
        tau, rated, mass = s.get("tau_peak_Nm"), s.get("tau_rated_Nm"), s.get("mass_kg")
        arm, rpm = s.get("armature_kgm2"), s.get("speed_noload_rpm")
        out: list[tuple[str, str, str, str]] = []

        if tau and mass:
            d = tau / mass
            lvl = "bad" if d > 200 else ("warn" if d > 120 else "good")
            out.append(("扭矩密度", f"{d:.0f} N·m/kg",
                        ">120 需复核，>200 不可信（受磁钢与散热限制）", lvl))
        else:
            out.append(("扭矩密度", "—", "缺峰值扭矩或质量，不推算", "na"))

        if tau and rated:
            pr = tau / rated
            lvl = "bad" if pr > 5 else ("warn" if pr > 3 else "good")
            out.append(("峰值/额定比", f"{pr:.1f}",
                        ">3 须给持续时间与初始温度，>5 基本等同堵转", lvl))
        else:
            out.append(("峰值/额定比", "—", "缺额定扭矩；不要假设它等于峰值的一半", "na"))

        if rpm:
            out.append(("空载角速度 ω", f"{rpm * 2 * 3.141592653589793 / 60:.1f} rad/s",
                        "× 腿长 = 腿尖速度上限", "good"))
        else:
            out.append(("空载角速度 ω", "—", "缺空载转速", "na"))

        if arm:
            # 反射惯量占比：需要一个腿的参考值。这里把假设写在判据里，不留暗箱。
            m_leg, l_leg = 2.0, 0.5
            app = arm + m_leg * (l_leg / 2) ** 2
            share = arm / app * 100
            lvl = "bad" if share > 70 else ("warn" if share > 45 else "good")
            out.append(("反射惯量占比", f"{share:.0f}%",
                        f"假设单腿 {m_leg} kg、腿长 {l_leg} m 绕髋摆；占比越高腿越「黏」", lvl))
        else:
            out.append(("反射惯量占比", "—", "缺转子惯量", "na"))
        return out

    from urllib.parse import quote_plus

    def resources(r: dict) -> str:
        """资料与链接。真有的放前面并标「官方」，其余标「检索入口」。"""
        s = r.get("specs") or {}
        q = quote_plus(f"{r['vendor']} {r['model']}")
        qz = quote_plus(f"{r['model']}")
        rows: list[tuple[str, str, str]] = []
        seen_urls: set[str] = set()

        if r.get("url"):
            rows.append(("官方页面 / 数据出处", r["url"], "本页数字的出处"))
            seen_urls.add(r["url"])
        if s.get("doc_url") and s["doc_url"] not in seen_urls:
            rows.append(("官方文档", s["doc_url"], "接口、引脚与系统说明"))
            seen_urls.add(s["doc_url"])
        if s.get("doc_pdf"):
            rows.append(("官方 PDF", s["doc_pdf"], "数据手册 / 使用说明书"))
            seen_urls.add(s["doc_pdf"])
        models = [u for u in (s.get("urdf_urls") or []) if u and u not in seen_urls]
        for i, u in enumerate(models, 1):
            name = "URDF / MJCF 模型" if i == 1 else f"URDF / MJCF 模型 {i}"
            rows.append((name, u, "官方 / 社区维护的整机模型，可直接导入 PyBullet、MuJoCo、Isaac"))
            seen_urls.add(u)
        repos = [u for u in (s.get("repo_urls") or []) if u and u not in seen_urls]
        for i, u in enumerate(repos, 1):
            name = "开源项目" if len(repos) == 1 else f"开源项目 {i}"
            rows.append((name, u, "官方 / 社区维护的 SDK、驱动与例程"))
            seen_urls.add(u)
        if s.get("image_source"):
            rows.append(("产品图出处", "", str(s["image_source"])))
        if r.get("origin"):
            rows.append(("收录说明", "", str(r["origin"])[:160]))

        # 以下都是**检索入口**，不是官方链接 —— 页面上会标明
        rows.append(("datasheet 检索", f"https://www.google.com/search?q={q}+datasheet",
                     "厂商常把 PDF 放在产品页附件里"))
        rows.append(("SDK / 驱动检索", f"https://github.com/search?q={qz}&type=repositories",
                     "找现成的 CAN 驱动与示例"))
        rows.append(("价格与货期检索", f"https://www.google.com/search?q={q}+%E4%BB%B7%E6%A0%BC",
                     "本站不卖货，报价请向厂商确认"))
        rows.append(("本站口径说明", "/semantics", "这些字段什么意思、缺了代表什么"))

        body = []
        for name, url, note in rows:
            if url:
                body.append(f'<tr><td><a href="{url}" target="_blank" rel="noopener">{name}</a></td>'
                            f'<td>{note}</td></tr>')
            else:
                body.append(f'<tr><td class="rs-plain">{name}</td><td>{note}</td></tr>')
        return ('<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead>'
                '<tbody>' + "".join(body) + "</tbody></table>")

    def advice(r: dict) -> list[tuple[str, str]]:
        """使用建议：全部由参数推算，页面上会标「按参数推断，非实测」。"""
        s = r.get("specs") or {}
        cat = r["category"]
        out: list[tuple[str, str]] = []
        tau = s.get("tau_peak_Nm")
        rated = s.get("tau_rated_Nm")
        rpm = s.get("speed_noload_rpm")
        gear = s.get("gear")
        arm = s.get("armature_kgm2")
        mass = s.get("mass_kg")

        if cat == "actuator":
            if arm:
                out.append(("仿真里填哪个字段",
                            f"MJCF/URDF 的 armature 字段填 **{num(arm, 4)}**"
                            f"（这是折算到输出端的等效惯量，与电机本体转子惯量差 N² 倍）。"
                            f"不要当转子惯量再乘 N² —— "
                            f"{'会差 ' + num((gear or 1) ** 2, 3) + ' 倍' if gear else '会差一个 N² 量级'}。"))
            if rpm:
                out.append(("腿尖速度上限",
                            f"空载 {num(rpm)} rpm ≈ {rpm * 0.10472:.1f} rad/s。"
                            f"腿长 0.4 m 时理论腿尖上限 ≈ {rpm * 0.10472 * 0.4:.1f} m/s；"
                            f"实际打 6 折再定目标速度。"))
            if tau and rated:
                pr = tau / rated
                if pr > 3:
                    out.append(("峰值只能用秒级",
                                f"峰值/额定 = {pr:.1f}。连续负载应当按额定 {num(rated)} N·m 设计，"
                                f"峰值只在加速/触地瞬间用。超 3 倍时必须向厂商要「持续时间 + 初始温度」。"))
                else:
                    out.append(("峰值与额定的用法",
                                f"峰值/额定 = {pr:.1f}，这个比值正常。"
                                f"连续按 {num(rated)} N·m、瞬时按 {num(tau)} N·m 设计即可。"))
            elif tau and not rated:
                out.append(("额定扭矩未知怎么办",
                            "只有峰值。按厂商惯例不要假设「额定 = 峰值/2」——"
                            "有的件是 3:1，有的只有 1.2:1。先向厂商要额定值再做热设计。"))
            if gear and gear >= 30:
                out.append(("高减速比的代价",
                            f"减速比 {num(gear)}，反射惯量会被放大。膝关节这类要快速摆动的关节，"
                            f"PD 里 kp 别照抄直驱参数，先用低 kp 高 kd 起步。"))
            elif gear and gear <= 10:
                out.append(("准直驱要配好电流环",
                            f"减速比只有 {num(gear)}，力矩靠电流直接给。"
                            f"电流环带宽低于 8 kHz 时，触地冲击会明显传到腿上。"))
            if mass and tau:
                out.append(("算你需要多大扭矩",
                            "静态站立（两腿支撑）单关节需求 ≈ 整机质量 × 9.81 × 腿长 / 4。"
                            "例：20 kg、腿长 0.4 m → 约 20 N·m 保持扭矩，"
                            "再乘 1.5–2 的安全系数才是你该选的额定值。"))
            if not s.get("price_cny"):
                out.append(("报价要自己问", "本站没有这个型号的公开价格。"
                            "同机座不同绕组的价差可能很小，但扭矩差很多 —— 问价时把型号后缀写全。"))

        elif cat == "controller_high":
            if s.get("npu_tops"):
                out.append(("算力口径", f"{num(s['npu_tops'])} TOPS 通常是 INT8。"
                            f"跑 FP16 的视觉模型按 1/2 估，跑 Transformer 策略还要再打折。"))
            if s.get("ram_gb"):
                out.append(("内存是硬门槛", f"{num(s['ram_gb'])} GB 要同时装相机流、点云和策略。"
                            f"做视觉重的方案直接看 16 GB 档。"))
            if s.get("power_max_w"):
                out.append(("功耗与散热", f"峰值 {num(s['power_max_w'])} W。"
                            f"整机电池与线束要按这个数留余量，别按典型功耗选。"))
        elif cat == "controller_low":
            if not s.get("foc_axes"):
                out.append(("这块不含 FOC 功率级",
                            "foc_axes 为空是因为板上没有集成电机驱动，不是漏填。"
                            "电机要外接电调/驱动器，选型时把电调的价格、体积和散热一起算进去。"))
            if s.get("current_loop_khz"):
                out.append(("力矩带宽", f"电流环 {num(s['current_loop_khz'])} kHz。"
                            f"做高动态力矩控制时，这个数比 MCU 主频更决定手感。"))
            if s.get("can"):
                out.append(("总线够不够", f"{s.get('can')} 路 CAN"
                            f"{'（支持 FD）' if s.get('canfd') else ''}。"
                            f"12 个关节 × 1 kHz 反馈，单路 CAN 2.0 会吃紧，优先 FD 或多路分载。"))
        elif cat == "imu":
            if s.get("odr_hz"):
                out.append(("ODR 与带宽", f"ODR {num(s['odr_hz'])} Hz。"
                            f"四足触地冲击的主要能量在 100–300 Hz，采样要够但别忘低通。"))
            out.append(("装在哪里", "尽量远离电机与减速器，或做温补 —— 四足跑久了 IMU 附近升温会有零偏漂移。"))
        elif cat == "structure":
            sub = r["subtype"]
            if sub in ("quadruped", "wheeled_quadruped",
                       "quadruped_inward_knee", "wheeled_quadruped_inward_knee"):
                if s.get("payload_kg") is not None:
                    out.append(("负载按行走工况算",
                                f"本行负载取 {num(s['payload_kg'])} kg（行走口径）。"
                                f"站立静载可能更高，但跑动、越障要按行走负载规划，别拿静载数当动态能力。"))
                if s.get("endurance_h") is not None:
                    out.append(("续航按最差工况留余量",
                                f"标称 {s['endurance_h']}。带载、爬坡、低温都会明显缩短，"
                                f"别把空载续航当成交付指标。"))
                if sub in ("wheeled_quadruped", "wheeled_quadruped_inward_knee"):
                    out.append(("轮足不是四足的替代",
                                "轮端适合平整路面高速移动；台阶、碎石、松软地面仍要靠足式步态。"
                                "选之前先列清楚任务地形里轮式与足式各占多少。"))
                else:
                    out.append(("腿构型决定越障与受力",
                                "全膝式、全肘式、前肘后膝（内膝肘）的关节受力与越障姿态不同；"
                                "同尺寸同质量也不能直接横比爬坡和续航。"))
                if s.get("climb_height_mm") is not None:
                    out.append(("爬高与爬坡分开看",
                                f"最大攀爬落差 {num(s['climb_height_mm'])} mm、爬坡 "
                                f"{num(s['climb_angle_deg'])}°。落差考验单腿摆高与关节峰值，"
                                f"爬坡考验持续扭矩与抓地。"))
            elif sub == "humanoid":
                if s.get("payload_kg") is not None:
                    out.append(("人形的负载是手臂负载",
                                f"标称 {num(s['payload_kg'])} kg 通常是单手臂最大负载，随伸展姿态变化；"
                                f"整机搬运能力要看厂商的整机负载口径。"))
                if s.get("dof") is not None:
                    out.append(("自由度决定动作空间",
                                f"{num(s['dof'])} 个关节。腰、腕、手是选配重点，"
                                f"下单前确认这个版本到底包含哪些自由度。"))
                out.append(("先确认是不是同一版本",
                            "同名人形常分标准版与 EDU / 开发版，自由度、算力、手部配置都不同，"
                            "价格也不同 —— 对比参数前先对齐版本。"))
            if not out:
                out.append(("整机参数不是部件参数",
                            "这一条收的是整机形态，用于对照平台方案；"
                            "关节电机、主控等部件请到对应品类里选。"))
        elif cat in ("camera", "lidar"):
            out.append(("先算视场与量程", "近距离抓地形看深度量程下限，别只看最大值；"
                        "楼梯这类弱纹理场景，结构光/ToF 与双目表现差别很大。"))
        elif cat == "module":
            out.append(("按子类看", "这一类是「其余模块」，字段不统一。"
                        "用之前先确认接口与供电，再谈精度。"))

        if not out:
            out.append(("暂无建议", "这个型号的关键参数还缺得多，先补齐再谈用法。"))
        return out

    METRIC_CLASS = {"good": "pm-good", "warn": "pm-warn", "bad": "pm-bad", "na": "pm-na"}

    def variants(r: dict) -> list[dict]:
        """同机座变体：同厂商 + 同外径的其他型号。

        这是最该看的一栏 —— 达妙 J4340 的 V1.0（27 N·m）和 V1.1（40 N·m）
        质量都是 0.362 kg，也就是说多出来的扭矩是绕组和电流换的，不是尺寸换的。
        按扭矩估质量的拟合式会在这里多收 30–47%。
        """
        s = r.get("specs") or {}
        od = s.get("od_mm")
        if not od:
            return []
        return [x for x in rows
                if x["id"] != r["id"] and x["category"] == "actuator"
                and x["vendor"] == r["vendor"]
                and (x.get("specs") or {}).get("od_mm") == od]

    n_part = 0
    for r in rows:
        cat, pid = r["category"], r["id"]
        s = r.get("specs") or {}
        fname = OUT / "parts" / cat / f"{slugs[pid]}.md"
        fname.parent.mkdir(parents=True, exist_ok=True)
        img = s.get("image_url")
        img_md = (f'<img src="{img}" alt="{r["model"]}" class="part-photo" />\n'
                  if img else "")
        conflicts = "【来源冲突】" in (r.get("notes") or "")

        # 官方参数一侧：只放关键字段，全部参数放到下面单独一节
        if cat == "camera":
            KEY = ["depth_range_m", "fov", "fps", "resolution", "iface",
                   "voltage_V", "power_w", "ip", "weight_g", "size_mm"]
        elif cat == "lidar":
            KEY = ["range_m", "fov", "points_per_s", "fps", "resolution", "iface",
                   "voltage_V", "power_w", "ip", "weight_g", "size_mm"]
        elif cat == "imu":
            KEY = ["gyro_range_dps", "accel_range_g", "odr_hz", "noise", "iface",
                   "voltage_V", "power_w", "weight_g", "size_mm"]
        elif cat == "structure":
            KEY = ["dof", "mass_kg", "payload_kg", "speed_max_mps", "size_mm",
                   "climb_height_mm", "climb_angle_deg", "battery", "endurance_h",
                   "voltage_V", "voltage_range_V", "iface", "compute", "sensors"]
        else:
            KEY = ["tau_peak_Nm", "tau_rated_Nm", "gear", "speed_noload_rpm", "mass_kg",
                   "armature_kgm2", "od_mm", "l_mm", "voltage_V", "kt_Nm_per_A",
                   "soc", "cpu", "cuda_cores", "npu_tops", "ram_gb", "power_max_w", "eth",
                   "mcu", "foc_axes", "can", "current_loop_khz", "voltage_max_V", "iface", "bits"]
        keyrows = "\n".join(
            f"| {SPEC_LABEL.get(k, k)} | "
            f"{'—' if s.get(k) is None else (s[k] if isinstance(s[k], str) else (format(int(s[k]), ',') if k == 'points_per_s' else num(s[k], 4)))} |"
            for k in KEY if k in s)
        if not keyrows:
            keyrows = "| — | 这一类暂无核心字段 |"

        # 社区一侧：评分组件（星标 + 分布 + 打分入口），评论由页尾 giscus 承担。
        # 不再写死「暂无评分」—— 组件自己判断：有后端读实时值，
        # 没有就读构建时烤的快照，都没有才显示空态。
        comm = f'''
<div class="part-comm">
<PartRating part-id="{pid}" />
</div>
'''

        advice_md = "\n".join(f"- **{t}** —— {b}" for t, b in advice(r))

        # 优惠：卡片上只显示「原价 + 优惠价」两个数，**条件全部写在这里**。
        # 关键：优惠不是人人都能用（学生证、参赛证明、限购台数），
        # 所以原价不划掉，两者并列；这里把每条的资格写清。
        ofs = offer_of(r)
        list_price = r.get("price_cny")
        if ofs:
            blocks = []
            for i, o in enumerate(ofs, 1):
                head = (f"**{num(o['price'], 0)} 元**（原价 {num(list_price, 0)} 元）"
                        if o.get("price") is not None
                        else f"**无固定优惠价**（原价 {num(list_price, 0)} 元）")
                blocks.append(
                    f"{i}. {head}\n"
                    f"   - 活动：{o.get('title') or '—'}\n"
                    f"   - 资格与条件：{o.get('condition') or '—'}\n"
                    f"   - 有效期：至 {o.get('expires') or '—'}\n"
                    f"   - 链接：{o.get('url') or '—'}\n"
                    f"   - 来源：{o.get('source') or '—'}"
                    + (chr(10) + "   - ⚠️ 示例条目（`demo: true`），发布前必须替换成真实合作信息。"
                       if o.get("demo") else ""))
            offer_md = (
                "::: warning 优惠需要资格，不是人人都能拿到\n"
                "下面每条的资格都写明。原价与优惠价并列展示，**不划掉原价** —— "
                "资格不满足时按原价算预算。\n\n"
                + "\n".join(blocks) + "\n:::")
        else:
            offer_md = ("暂无优惠信息。本站不代理销售，也不收佣金 —— "
                        "有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，"
                        "缺一项都不上卡片。")

        # 关节电机的深度指标
        metric_md = ""
        if cat == "actuator":
            mr = metrics(r)
            body = "\n".join(
                f'<div class="pm-row">'
                f'<span class="pm-k">{k}</span>'
                f'<span class="pm-v">{v}</span>'
                f'<span class="pm-note">{n}</span></div>'
                for k, v, n, lvl in mr)
            metric_md = f"""
## 选型指标

<div class="pm-table">
{body}
</div>

::: tip 怎么用这三行
**扭矩密度**决定「同样扭矩下多重」；**峰值/额定比**决定「这个数能信多久」；
**反射惯量占比**决定「这条腿能不能快速摆动」。
三者一起看，比单看峰值扭矩有用得多 —— 高减速比件通常前两项好看、第三项很糟。
:::
"""

        # 同机座变体
        var_md = ""
        vs = variants(r)
        if vs:
            vrows = "\n".join(
                f"| [{x['model']}](/{'parts'}/{x['category']}/{slugs[x['id']]}) "
                f"| {num((x.get('specs') or {{}}).get('tau_peak_Nm'))} "
                f"| {num((x.get('specs') or {{}}).get('mass_kg'))} "
                f"| {num((x.get('specs') or {{}}).get('gear'))} |"
                for x in vs)
            var_md = f"""
## 同机座变体（外径 {num(s.get('od_mm'))} mm）

同一个机座上换绕组 / 换减速比出来的型号。**质量往往一样，扭矩可以差 50% 以上** ——
多出来的扭矩是电流换的，不是尺寸换的，所以别按扭矩去估质量。

| 型号 | 峰值 τ N·m | 质量 kg | 减速比 |
|---|---|---|---|
{vrows}
"""

        fname.write_text(FRONT.format(title=f'{r["vendor"]} {r["model"]}') + f"""
# {r["vendor"]} {r["model"]}

<div class="part-hero">
  <div class="part-hero-left">
    {img_md}
  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">{CAT_LABEL.get(cat, cat)}</span>
      <span class="part-tag sub">{r.get("subtype_label") or r["subtype"]}</span>
      <span class="part-tag tier{r["source_tier"]}">来源 {r["source_tier"]}{" ✓ 已核对" if r["verified"] else ""}</span>
      {f'<span class="part-tag">¥{int(r["price_cny"]):,}</span>' if r.get("price_cny") else '<span class="part-tag muted">无公开报价</span>'}
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
{keyrows}

<div class="part-src">
来源：<a href="{r.get("url") or "#"}">{r.get("url") or "—"}</a><br/>
收录：{r.get("origin") or "—"}<br/>
核对：{r.get("last_checked") or "—"}
</div>

</div>
{comm}
</div>
  </div>
</div>

{"::: warning 来源冲突" + chr(10) + "这份数据的来源之间有分歧，未经覆盖，写在下方「备注」里。" + chr(10) + ":::" + chr(10) if conflicts else ""}
## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

{advice_md}

{metric_md}
{var_md}
## 全部参数

| 字段 | 值 |
|---|---|
{spec_rows(s, r["category"])}

## 优惠与获取条件

{offer_md}

## 资料与链接

{resources(r)}

## 备注

{r.get("notes") or "—"}

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
""", encoding="utf-8")
        n_part += 1
    print(f"  型号页 {n_part} 个（每页底下挂 giscus 讨论）")

    sidebar: dict[str, list] = {}
    n_act = sum(1 for r in rows if r["category"] == "actuator")
    n_img = sum(1 for r in rows if (r.get("specs") or {}).get("image_url"))
    n_arm = sum(1 for r in rows if (r.get("specs") or {}).get("armature_kgm2"))
    n_rated = sum(1 for r in rows if (r.get("specs") or {}).get("tau_rated_Nm"))
    vendors = sorted({r["vendor"] for r in rows if r["category"] == "actuator"})

    # ── 首页：这是社区，不是说明书 ──────────────────────────────────────
    n_rated_pct = round(n_rated / n_act * 100) if n_act else 0
    n_arm_pct = round(n_arm / n_act * 100) if n_act else 0
    cat_cards = "\n".join(
        f'<a class="hc" href="/parts/{c}/"><b>{name}</b>'
        f'<span>{sum(1 for r in rows if r["category"] == c) or "待收录"}</span>'
        f'<em>{desc}</em></a>'
        for c, name, desc in CATS)
    (OUT / "index.md").write_text(
        '---\nlayout: page\nsidebar: false\noutline: false\ntitleTemplate: false\n---\n\n'
        + f'''
<div class="home">
  <section class="home-hero">
    <div class="home-kicker">机器人部件选择社区</div>
    <h1>选部件，先看参数，再看<em>用过的人怎么说</em>。</h1>
    <p>
      每个部件一页：左边是官方参数（带来源等级与口径），右边是真实使用者的评分与评价。
      不收佣金、不卖零件，所以判定不必讨好谁。
    </p>
    <div class="home-cta">
      <a class="home-btn" href="/catalog">进部件库 →</a>
      <a class="home-btn ghost" href="/semantics">参数口径怎么读</a>
    </div>
  </section>

  <section class="home-stats">
    <div><b>{len(rows)}</b><span>在库部件</span></div>
    <div><b>{n_act}</b><span>关节电机 · {len(vendors)} 家</span></div>
    <div><b>{n_arm_pct}%</b><span>有转子惯量（可直接进仿真）</span></div>
    <div><b>{n_rated_pct}%</b><span>有额定扭矩</span></div>
  </section>

  <section class="home-cats">
    <h2>按品类</h2>
    <div class="home-cat-grid">{cat_cards}</div>
    <p class="home-note">
      「待收录」不是漏了 —— 是没有可信来源。宁可空着，也不拿论文里的典型值充数。
    </p>
  </section>

  <section class="home-how">
    <h2>这一页该怎么用</h2>
    <div class="home-how-grid">
      <div>
        <b>1 · 先看官方参数</b>
        <p>来源等级 <code>A</code> 表示逐项对过厂商手册。缺的字段写 <code>—</code>，
        不猜、不用额定代替峰值。每个数都能查到「谁在什么时候、凭什么改成了现在这样」。</p>
      </div>
      <div>
        <b>2 · 再看使用者的分</b>
        <p>评分走 GitHub issue，<strong>一人一件一票</strong>，装过机的单独统计。
        评论在部件页底部（GitHub Discussions），用来说明「为什么给这个分」。</p>
      </div>
      <div>
        <b>3 · 别只看峰值扭矩</b>
        <p>部件页会算扭矩密度、峰值/额定比、反射惯量占比。高减速比件通常前两项好看、
        第三项很糟 —— 那条腿会很「黏」。</p>
      </div>
    </div>
  </section>

  <section class="home-links">
    <a href="/parts/">按厂商浏览</a>
    <a href="/semantics">参数口径</a>
    <a href="/sources">数据来源与纪律</a>
  </section>
</div>

<style>
.home {{ max-width: 1180px; margin: 0 auto; padding: 2.2rem 1.5rem 4rem; }}
.home-hero {{ padding: 1.2rem 0 1.8rem; border-bottom: 1px solid var(--vp-c-divider); }}
.home-kicker {{
  font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--vp-c-brand-1); font-weight: 700; margin-bottom: 0.6rem;
}}
.home-hero h1 {{
  font-size: clamp(1.6rem, 3.4vw, 2.5rem); line-height: 1.25; font-weight: 800;
  letter-spacing: -0.02em; margin: 0 0 0.8rem; border: none; padding: 0;
  color: var(--vp-c-text-1);
}}
.home-hero h1 em {{
  font-style: normal;
  background: linear-gradient(135deg, var(--vp-c-brand-1), #4fc1ff);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}}
.home-hero p {{ margin: 0 0 1.2rem; max-width: 62ch; font-size: 0.92rem;
  line-height: 1.85; color: var(--vp-c-text-2); }}
.home-cta {{ display: flex; gap: 0.6rem; flex-wrap: wrap; }}
.home-btn {{
  font-size: 0.86rem; font-weight: 600; padding: 0.5rem 1.05rem; border-radius: 999px;
  background: var(--vp-c-brand-1); color: #fff; text-decoration: none;
}}
.home-btn.ghost {{
  background: transparent; color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-divider);
}}
.home-btn:hover {{ text-decoration: none; opacity: 0.92; }}

.home-stats {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1px; background: var(--vp-c-divider);
  border: 1px solid var(--vp-c-divider); border-radius: 12px; overflow: hidden;
  margin: 1.6rem 0;
}}
.home-stats > div {{ background: var(--vp-c-bg); padding: 0.9rem 1rem; }}
.home-stats b {{
  display: block; font-size: 1.5rem; font-weight: 800; line-height: 1.1;
  color: var(--vp-c-brand-1); font-variant-numeric: tabular-nums;
}}
.home-stats span {{ font-size: 0.74rem; color: var(--vp-c-text-3); }}

.home h2 {{
  font-size: 1.02rem; font-weight: 700; margin: 0 0 0.8rem;
  border: none; padding: 0; color: var(--vp-c-text-1);
}}
.home-cat-grid {{
  display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 0.5rem;
}}
.hc {{
  display: flex; flex-direction: column; gap: 2px;
  border: 1px solid var(--vp-c-divider); border-radius: 10px;
  padding: 0.6rem 0.7rem; text-decoration: none;
  background: var(--vp-c-bg); transition: border-color 0.18s, transform 0.18s;
}}
.hc:hover {{ border-color: var(--vp-c-brand-1); transform: translateY(-2px); text-decoration: none; }}
.hc b {{ font-size: 0.84rem; color: var(--vp-c-text-1); }}
.hc span {{ font-size: 0.74rem; color: var(--vp-c-brand-1); font-variant-numeric: tabular-nums; }}
.hc em {{ font-size: 0.7rem; font-style: normal; color: var(--vp-c-text-3); }}
.home-note {{ font-size: 0.74rem; color: var(--vp-c-text-3); margin-top: 0.7rem; }}

.home-how-grid {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.8rem;
  margin-top: 0.4rem;
}}
.home-how-grid > div {{
  border-left: 3px solid var(--vp-c-brand-soft); padding: 0.1rem 0 0.1rem 0.8rem;
}}
.home-how-grid b {{ font-size: 0.84rem; color: var(--vp-c-text-1); }}
.home-how-grid p {{ font-size: 0.78rem; line-height: 1.8; color: var(--vp-c-text-2); margin: 0.3rem 0 0; }}
.home-links {{
  display: flex; flex-wrap: wrap; gap: 1.1rem; margin-top: 2.2rem;
  padding-top: 1.1rem; border-top: 1px solid var(--vp-c-divider);
  font-size: 0.8rem;
}}
.home-links a {{ color: var(--vp-c-brand-1); }}
</style>
''', encoding="utf-8")

    # ── 部件总表 ────────────────────────────────────────────────────────
    cat_links = "\n".join(f"- **[{name}](/parts/{c}/)** —— {desc}（{sum(1 for r in rows if r['category'] == c)} 件）"
                          for c, name, desc in CATS)
    (OUT / "parts" / "index.md").write_text(FRONT.format(title="部件详情") + f"""
# 部件详情

按品类进入，再按厂商分页。

{cat_links}

每一页底下都有一条讨论串 —— 用过的坑、量到的数、和厂商确认过的事，写在对应那页下面才有用。
""", encoding="utf-8")

    for c, name, desc in CATS:
        items = [r for r in rows if r["category"] == c]
        if c == "actuator":
            vs = sorted({r["vendor"] for r in items})
            (OUT / "parts" / c / "index.md").write_text(
                FRONT.format(title=name) + f"""
# {name}

{desc}，共 **{len(items)}** 件、**{len(vs)}** 家厂商。

## 厂商

""" + "\n".join(
                    f"- [{'/'.join(['', 'parts', c, slug(v)])}]({('/parts/' + c + '/' + slug(v))}) —— "
                    f"{v}（{sum(1 for r in items if r['vendor'] == v)} 型）" for v in vs)
                + f"""

## 跨厂商速览（按峰值扭矩降序，前 40）

{actuator_table(sorted(items, key=lambda r: -(r['specs'].get('tau_peak_Nm') or 0))[:40])}

> 完整 147 行在[选型台](/)按任意列排序。这里只放前 40，因为一张表读不完等于没读。
""", encoding="utf-8")

            # 每家一页
            for v in vs:
                sub = [r for r in items if r["vendor"] == v]
                note = ""
                notes = [r["notes"] for r in sub if "来源冲突" in (r.get("notes") or "")]
                if notes:
                    note = "\n::: warning 来源冲突\n" + "\n\n".join(
                        n.split("【来源冲突】")[-1][:400] for n in notes[:3]) + "\n:::\n"
                (OUT / "parts" / c / f"{slug(v)}.md").write_text(
                    FRONT.format(title=v) + f"""
# {v}

共 **{len(sub)}** 型。数据等级 `A` 表示来自厂商手册/规格书且已逐项核对过。
{note}
{actuator_table(sub)}

## 这一页的讨论

用过的、量到的、和厂商确认过的，写在下面。**带上具体工况**（负载、占空比、环境温度），
只写「好用/不好用」对下一个人没有价值。
""", encoding="utf-8")
        elif c == "structure":
            sections = []
            for st, label, note in STRUCTURE_SUBTYPES:
                sub = [r for r in items if r["subtype"] == st]
                if sub:
                    sections.append(
                        f"## {label} {{#{st}}}\n\n{note}，共 **{len(sub)}** 款。\n\n"
                        + generic_table(sub, c))
                else:
                    sections.append(
                        f"## {label} {{#{st}}}\n\n{note}。暂无收录 —— 没有可信来源，宁缺不编。")
            n_sub = len({r["subtype"] for r in items})
            (OUT / "parts" / c / "index.md").write_text(
                FRONT.format(title=name) + f"""
# {name}

按机器人形态分类收录整机，共 **{len(items)}** 款、**{n_sub}** 种形态。
轮足与足式的通过性、续航、负载口径不同，先按任务地形选形态，再横比参数。

{(chr(10) * 2).join(sections)}
""", encoding="utf-8")
        else:
            n_b = sum(1 for r in items if r["source_tier"] != "A")
            tier_note = (f"\n> 其中 {n_b} 行是 `B` 级（来自公开文档/官网，未逐项核对），"
                         f"采购前请回原厂页面确认。\n" if n_b else "")
            (OUT / "parts" / c / "index.md").write_text(
                FRONT.format(title=name) + f"""
# {name}

{desc}，共 **{len(items)}** 件。

{generic_table(items, c)}
{tier_note}""", encoding="utf-8")


    # ── 参数口径（直接 import 后端的常量，杜绝漂移）──────────────────
    import sys
    sys.path.insert(0, str(ROOT / "backend"))
    from app.api.routes.semantics import (  # noqa: E402
        COMPARABILITY, CONVERSIONS, FIELD_SEMANTICS, RED_LINES,
        SUPPLIER_QUESTIONS, TRINARY,
    )

    def rows3(items, cols):
        head = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols)
        body = []
        for it in items:
            body.append("| " + " | ".join(
                str(it.get(c, "") if not isinstance(it.get(c), list)
                    else "、".join(map(str, it[c]))) for c in cols) + " |")
        return head + "\n" + "\n".join(body)

    field_rows = [{"field": k, **v} for k, v in FIELD_SEMANTICS.items()]
    section_redlines = rows3(RED_LINES, ["id", "name", "why"])
    section_conv = rows3(CONVERSIONS, ["from", "to", "formula"])
    section_comp = rows3(COMPARABILITY, ["grade", "name", "condition"])
    section_field = rows3(field_rows, ["field", "label", "meaning"])
    section_ask = "\n".join(f"{i}. {q}" for i, q in enumerate(SUPPLIER_QUESTIONS, 1))

    # 红线做成卡片：6 列表格在小屏上没法读，而这一节是最该被读完的
    def redline_cards() -> str:
        out = []
        for it in RED_LINES:
            thr = ""
            if it.get("review_above") is not None:
                thr = (f'<span class="rl-th"><b>{it["review_above"]}</b> 需复核 · '
                       f'<b>{it["absurd_above"]}</b> 不可信</span>')
            formula = f'<code>{it["formula"]}</code>' if it.get("formula") else ""
            out.append(f'''<div class="rl">
  <div class="rl-head"><span class="rl-id">{it['id']}</span><b>{it['name']}</b>{formula}</div>
  {thr}
  <p class="rl-why">{it['why']}</p>
  <p class="rl-how"><span>怎么核</span>{it['how_to_check']}</p>
</div>''')
        return "\n".join(out)

    # 字段字典按用途分组，别一长条
    FGROUP = [
        ("扭矩与转速", ["tau_peak_Nm", "tau_rated_Nm", "tau_basis", "speed_noload_rpm",
                    "speed_rated_rpm", "gear"]),
        ("惯量与质量", ["mass_kg", "armature_kgm2", "rotor_inertia_kgm2", "inertia_basis",
                    "od_mm", "l_mm"]),
        ("电气", ["voltage_V", "voltage_range_V", "kt_Nm_per_A", "r_phase_ohm",
                "l_phase_uh", "pole_pairs", "i_peak_A", "i_rated_A"]),
        ("接口与防护", ["encoder", "comm", "driver_integrated", "ip"]),
    ]
    field_groups = []
    seen_fields = set()
    for gname, keys in FGROUP:
        # 注意：变量名不能叫 rows —— 外层 rows 是零件列表，覆盖了侧边栏就没厂商了
        fd_rows = []
        for k in keys:
            v = FIELD_SEMANTICS.get(k)
            if not v:
                continue
            seen_fields.add(k)
            fd_rows.append(f'''<div class="fd">
  <div class="fd-head"><code>{k}</code><b>{v.get('label','')}</b></div>
  <p>{v.get('meaning','')}</p>
  <p class="fd-miss"><span>缺了意味着</span>{v.get('missing_means','—')}</p>
</div>''')
        if fd_rows:
            field_groups.append(f'<h3>{gname}</h3><div class="fd-grid">{"".join(fd_rows)}</div>')
    rest = [f'''<div class="fd"><div class="fd-head"><code>{k}</code><b>{v.get('label','')}</b></div>
  <p>{v.get('meaning','')}</p>
  <p class="fd-miss"><span>缺了意味着</span>{v.get('missing_means','—')}</p></div>'''
            for k, v in FIELD_SEMANTICS.items() if k not in seen_fields]
    if rest:
        field_groups.append(f'<h3>其他</h3><div class="fd-grid">{"".join(rest)}</div>')

    (OUT / "semantics.md").write_text(
        '---\ntitle: 参数口径\nlayout: page\nsidebar: false\noutline: false\n---\n\n'
        + f'''
<div class="sem">
  <header class="sem-hero">
    <div class="sem-kicker">参数口径</div>
    <h1>同一个数，在不同厂商嘴里不是同一件事。</h1>
    <p>
      「峰值扭矩 40 N·m」可能指瞬时 1 秒、也可能指持续堵转；
      「质量 0.362 kg」可能含线缆、也可能只是定转子。
      这一页把所有字段的<b>定义、缺口含义、以及该停下来复核的阈值</b>写清楚，
      也提供机器可读版本（<code>GET /api/semantics</code>，MCP 工具直接复用）。
    </p>
  </header>

  <section class="sem-steps">
    <div><b>1</b><span>先看<em>来源等级</em></span><p><code>A</code> 逐项对过厂商手册；<code>B</code> 来自公开网页；<code>C</code> 转述。等级决定你敢不敢直接用它做热设计。</p></div>
    <div><b>2</b><span>再看<em>口径字段</em></span><p><code>tau_basis</code> 是 peak 还是 rated、<code>inertia_basis</code> 是 rotor 还是 output。这两个字段读错，后面全错。</p></div>
    <div><b>3</b><span>缺的要当缺的</span><p><code>—</code> 是「没公布」，不是「不支持」，也不是 0。不要用同类件填补，也不要假设额定 = 峰值 / 2。</p></div>
    <div><b>4</b><span>最后才比<em>派生量</em></span><p>扭矩密度、峰值/额定比、反射惯量占比 —— 这三个是结果，不是原因；它们帮你发现异常，不帮你选型。</p></div>
  </section>

  <section>
    <h2>判定只有三种结论</h2>
    <div class="sem-tri">
      <span class="tri yes">{TRINARY['values'][0]}</span>
      <span class="tri no">{TRINARY['values'][1]}</span>
      <span class="tri unknown">{TRINARY['values'][2]}</span>
    </div>
    <p class="sem-note">{TRINARY.get('unknown_means', '证据不足，既不算兼容也不算不兼容。')}</p>
  </section>

  <section>
    <h2>六条物理红线</h2>
    <div class="rl-grid">{redline_cards()}</div>
  </section>

  <section>
    <h2>字段字典</h2>
    {"".join(field_groups)}
  </section>

  <section>
    <h2>单位换算</h2>
    {section_conv}
    <p class="sem-note">转速的两种写法量纲互逆（<code>sec/60°</code> 与 <code>rpm</code>），
    按数值直接比会得到相反结论。</p>
  </section>

  <section>
    <h2>可比性分级</h2>
    {section_comp}
  </section>

  <section>
    <h2>向供应商问询清单</h2>
    <p class="sem-note">可直接粘进技术协议或询价邮件。写不进合同的参数，验收时不具备约束力。</p>
    {section_ask}
  </section>
</div>

<style>
.sem {{ max-width: 1080px; margin: 0 auto; padding: 1.8rem 1.5rem 4rem; }}
.sem-kicker {{
  font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--vp-c-brand-1); font-weight: 700; margin-bottom: 0.5rem;
}}
.sem-hero h1 {{
  font-size: clamp(1.4rem, 2.6vw, 1.9rem); line-height: 1.3; font-weight: 800;
  letter-spacing: -0.02em; margin: 0 0 0.7rem; border: none; padding: 0;
  color: var(--vp-c-text-1);
}}
.sem-hero p {{ margin: 0; font-size: 0.86rem; line-height: 1.85;
  color: var(--vp-c-text-2); max-width: 70ch; }}
.sem h2 {{
  font-size: 1.02rem; font-weight: 700; margin: 2rem 0 0.75rem;
  border: none; padding: 0; color: var(--vp-c-text-1);
}}
.sem h3 {{ font-size: 0.86rem; font-weight: 600; margin: 1.1rem 0 0.5rem;
  color: var(--vp-c-text-2); }}

.sem-steps {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 0.7rem; margin: 1.6rem 0 0;
}}
.sem-steps > div {{
  border: 1px solid var(--vp-c-divider); border-radius: 10px;
  padding: 0.7rem 0.8rem; background: var(--vp-c-bg);
}}
.sem-steps b {{
  display: inline-flex; align-items: center; justify-content: center;
  width: 18px; height: 18px; border-radius: 999px; font-size: 0.68rem;
  background: var(--vp-c-brand-soft); color: var(--vp-c-brand-1); margin-bottom: 0.35rem;
}}
.sem-steps span {{ display: block; font-size: 0.82rem; font-weight: 600;
  color: var(--vp-c-text-1); }}
.sem-steps em {{ font-style: normal; color: var(--vp-c-brand-1); }}
.sem-steps p {{ margin: 0.3rem 0 0; font-size: 0.76rem; line-height: 1.75;
  color: var(--vp-c-text-3); }}

.sem-tri {{ display: flex; gap: 0.4rem; }}
.tri {{
  font-size: 0.78rem; font-weight: 700; padding: 0.2rem 0.7rem; border-radius: 999px;
  font-family: var(--font-mono, monospace);
}}
.tri.yes {{ background: var(--vp-c-brand-soft); color: var(--vp-c-brand-1); }}
.tri.no {{ background: rgba(192, 43, 43, 0.1); color: #c02b2b; }}
html.dark .tri.no {{ background: rgba(244, 135, 113, 0.14); color: #f48771; }}
.tri.unknown {{ background: var(--vp-c-default-soft); color: var(--vp-c-text-3); }}
.sem-note {{ font-size: 0.76rem; line-height: 1.8; color: var(--vp-c-text-3);
  margin: 0.5rem 0 0; }}

.rl-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 0.6rem; }}
.rl {{ border: 1px solid var(--vp-c-divider); border-radius: 10px;
  padding: 0.65rem 0.8rem; background: var(--vp-c-bg); }}
.rl-head {{ display: flex; align-items: baseline; gap: 0.45rem; flex-wrap: wrap; }}
.rl-id {{ font-size: 0.66rem; font-weight: 700; color: var(--vp-c-text-3);
  font-family: var(--font-mono, monospace); }}
.rl-head b {{ font-size: 0.84rem; color: var(--vp-c-text-1); }}
.rl-head code {{ font-size: 0.7rem; }}
.rl-th {{ display: block; font-size: 0.72rem; color: #a06a00; margin-top: 0.25rem; }}
html.dark .rl-th {{ color: #e0b159; }}
.rl-th b {{ font-variant-numeric: tabular-nums; }}
.rl-why {{ font-size: 0.76rem; line-height: 1.75; color: var(--vp-c-text-2); margin: 0.35rem 0 0; }}
.rl-how {{ font-size: 0.72rem; line-height: 1.7; color: var(--vp-c-text-3); margin: 0.3rem 0 0; }}
.rl-how span {{ display: inline-block; font-weight: 600; color: var(--vp-c-brand-1);
  margin-right: 0.35rem; }}

.fd-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 0.55rem; }}
.fd {{ border-left: 2px solid var(--vp-c-brand-soft); padding: 0.1rem 0 0.1rem 0.7rem; }}
.fd-head {{ display: flex; align-items: baseline; gap: 0.4rem; }}
.fd-head code {{ font-size: 0.72rem; }}
.fd-head b {{ font-size: 0.8rem; color: var(--vp-c-text-1); }}
.fd p {{ margin: 0.25rem 0 0; font-size: 0.75rem; line-height: 1.7; color: var(--vp-c-text-2); }}
.fd-miss {{ color: var(--vp-c-text-3) !important; }}
.fd-miss span {{ font-weight: 600; margin-right: 0.35rem; }}

.sem table {{ font-size: 0.78rem; }}
.sem table td, .sem table th {{ white-space: normal; }}
.sem ol {{ font-size: 0.8rem; line-height: 1.9; color: var(--vp-c-text-2); }}
</style>
''', encoding="utf-8")

    # ── 数据来源 ────────────────────────────────────────────────────────
    srcs = [
        ("达妙科技 2026 产品选型手册", "31 型 J/JH/D 系列，逐页解析", "本地 PDF"),
        ("灵足时代 RS / EL 系列规格介绍", "9 型，含 2026-10 修订的重量", "本地 PDF"),
        ("Draft（davidhnguyen2000/draft）", "114 行目录 + 拟合趋势 + MuJoCo 模型", "GitHub，MIT"),
        ("CubeMars / MyActuator 官网", "按产品页 og:image 抓参数与图", "在线抓取"),
        ("ZJU-HelloWorld/Wiki", "DJI RM 三型的额定/堵转扭矩，宇树手册", "GitHub，附厂商 PDF"),
        ("yssickjgd/robowalker_train", "协议定标常量、M3508 精确减速比", "GitHub"),
        ("roboparts.cc", "接口形态（MCP、三态判定、证据分级）", "参考设计，未取数据"),
        ("LeRobotDepot / Humanoid Atlas", "价格三件套、受控枚举", "参考设计，未取数据"),
    ]
    srow = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in srcs)
    (OUT / "sources.md").write_text(FRONT.format(title="数据来源") + f"""
# 数据来源

| 来源 | 取走了什么 | 形态 |
|---|---|---|
{srow}

## 我们拒绝做的事

1. **不灌示例评价。** 曾经灌过 21 条「实测」，技术观察是真的，但温度、时长、作者都是编的。
   在一个立意是「真实使用信息」的站里，这比空着坏得多。已全部删除。
2. **不改数值来掩盖冲突。** 宇树 A1 的减速比，官网写 6:1、手册写 1:9，
   两个都留着，标成「来源冲突」。
3. **不为了过校验编一个峰值。** GM6020 手册只给额定扭矩，峰值就写 `—`，
   并为这种情况放宽了数据闸门的规则。
4. **不混用电调口径。** M2006 的堵转 7 N·m 只在 Z650 那张表里，
   与 C610 的额定 1 N·m 不同源，不拼成一个「峰值/额定比」。

## 每个数字的追溯链

零件的每次字段改动都写进 `part_edits` 表（旧值、新值、依据、来源链接、谁改的、何时）。
于是任何一个数都能回答：**它什么时候、被谁、凭什么被改成了现在这样。**
""", encoding="utf-8")

    # ── 侧边栏 ──────────────────────────────────────────────────────────
    act_items = [{"text": "总览", "link": "/parts/actuator/"}]
    for v in sorted({r["vendor"] for r in rows if r["category"] == "actuator"}):
        act_items.append({"text": v, "link": f"/parts/actuator/{slug(v)}"})
    sidebar["/parts/"] = [
        {"text": "部件手册", "items": [
            {"text": "索引", "link": "/parts/"},
            {"text": "关节电机", "collapsed": False, "items": act_items},
        ]},
    ]
    # 其余品类按 CATS 生成（含暂无数据的：点进去是「未收录」说明页，
    # 这样读者知道这一类存在但还没收，而不是以为漏了）
    for c, name, _ in CATS:
        if c == "actuator":
            continue
        if c == "structure":
            sub_items = [{"text": "总览", "link": "/parts/structure/"}]
            for st, label, _ in STRUCTURE_SUBTYPES:
                n = sum(1 for r in rows
                        if r["category"] == "structure" and r["subtype"] == st)
                sub_items.append({
                    "text": f"{label}（{n}）" if n else f"{label}（待收录）",
                    "link": f"/parts/structure/#{st}",
                })
            sidebar["/parts/"][0]["items"].append(
                {"text": name, "collapsed": False, "items": sub_items})
        else:
            sidebar["/parts/"][0]["items"].append(
                {"text": name, "link": f"/parts/{c}/"})

    sem = json.loads((DATA / ".." / "backend" / "app" / "api" / "routes" /
                      "_semantics_cache.json").read_text(encoding="utf-8")) \
        if (ROOT / "backend" / "app" / "api" / "routes" / "_semantics_cache.json").exists() else None

    (OUT / ".vitepress").mkdir(parents=True, exist_ok=True)
    (OUT / ".vitepress" / "sidebar.json").write_text(
        json.dumps(sidebar, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"生成 {len(list(OUT.rglob('*.md')))} 个页面")
    print(f"  侧边栏 {sum(len(g[0]['items']) for g in sidebar.values())} 组")
    print(f"  执行器 {n_act} 件 / {len(vendors)} 家")


if __name__ == "__main__":
    main()
