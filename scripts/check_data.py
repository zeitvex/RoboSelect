#!/usr/bin/env python3
"""数据闸门：在把 data/*.json 灌进库之前，先拦住口径不一致。

    python scripts/check_data.py          # 退出码 0 = 全部通过
    python scripts/check_data.py --strict # 把 warning 也当失败

这套检查是这几份参考项目踩过的坑的直接产物：
  * RoboParts 的库里 torque 有 19 种表述口径、speed 有 37 种 → 这里强制 tau_basis
  * RoboParts 的库里没有一条数据达到「可直接比较」 → 这里强制 source_tier
  * sbc-reviews 的 arch 字段漂成 aarch64/arm64 两种拼法 → 这里强制枚举
  * Draft 的 `kind: output` 读错会让 armature 错 10⁴ 倍 → 这里强制复算校验
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

TIERS = {"A", "B", "C"}
TAU_BASIS = {"peak", "rated"}
INERTIA_BASIS = {"rotor", "output"}

# 数值字段白名单：出现没见过的小写驼峰/拼写错误时报警，防止词表漂移
KNOWN_SPEC_KEYS = {
    # 执行器
    "tau_peak_Nm", "tau_rated_Nm", "tau_basis", "speed_noload_rpm", "speed_rated_rpm",
    "gear", "mass_kg", "od_mm", "l_mm", "rotor_inertia_kgm2", "inertia_basis",
    "armature_kgm2", "voltage_V", "voltage_range_V", "kt_Nm_per_A", "r_phase_ohm",
    "l_phase_uh", "pole_pairs", "i_peak_A", "i_rated_A", "frictionloss_Nm",
    "damping_Nms_rad", "encoder", "comm", "driver_integrated", "ip",
    "image_url", "image_source",
    # 上位机
    "soc", "cpu", "cores", "cpu_arch", "gpu", "cuda_cores", "npu_tops", "ram_gb",
    "ram_bw_gbs", "storage_gb", "power_idle_w", "power_max_w", "os", "cuda", "ros2",
    "eth", "usb", "can", "csi", "pcie", "size_mm", "weight_g",
    # 下位机
    "mcu", "clock_mhz", "ram_kb", "flash_kb", "foc_axes", "canfd",
    "current_loop_khz", "torque_mode", "voltage_in_V", "voltage_max_V", "comm_upper",
    # 资料链接（上下位机共用；不进参数表，只在「资料」里渲染）
    "doc_url", "doc_pdf", "repo_urls", "urdf_urls",
    # 传感器
    "gyro_range_dps", "accel_range_g", "odr_hz", "iface", "noise", "resolution",
    "depth_range_m", "fps", "fov", "range_m", "points_per_s", "channel", "bits",
    "absolute", "temp_range_C",
    # 机械结构（整机形态）
    "dof", "payload_kg", "speed_max_mps", "climb_height_mm", "climb_angle_deg",
    "endurance_h", "battery", "compute", "sensors",
    # 归档导入用到的字段（见 scripts/normalize_archive.py 的 FIELD_MAP）
    "tau_stall_Nm", "tau_hold_Nm", "i_stall_A", "dims", "temp_range",
    "storage_temp_range", "meas_range", "accuracy", "response_time", "power_w",
    "motor_type", "gear_material", "housing_material", "bearing", "mounting",
    "connector", "backlash_arcmin",
}

#: UI 真正会读的键。B 级行字段参差，只要求这些键存在（值可为 null），
#: 少了会渲染出空白而不是「—」，所以单独提示。
UI_KEYS = {
    "actuator": {"tau_peak_Nm", "tau_rated_Nm", "gear", "mass_kg", "voltage_V",
                 "speed_noload_rpm", "image_url"},
    "lidar": {"range_m", "image_url"},
    "camera": {"depth_range_m", "image_url"},
    "imu": {"odr_hz", "image_url"},
    "module": {"image_url"},
    "controller_high": {"image_url"},
    "controller_low": {"image_url"},
    "structure": {"dof", "mass_kg", "payload_kg", "speed_max_mps", "image_url"},
}

# 阈值（来自 RoboParts《关节参数虚标怎么辨别》的物理红线）
TD_REVIEW = 120.0      # 额定扭矩密度 > 120 N·m/kg 需复核
TD_ABSURD = 200.0      # 峰值扭矩密度 > 200 N·m/kg 几乎不可信
PR_REVIEW = 3.0        # 峰值/额定 > 3 需给持续时间
PR_ABSURD = 5.0        # > 5 基本是瞬时堵转值

# 物理量程闸门：超出去几乎一定是单位/解析错误，不是产品差异
# （这些边界就是被 μ/µ 两个码点坑过一次之后加的）
PLAUSIBLE = {
    "mass_kg": (0.005, 100.0),
    "od_mm": (10.0, 1000.0),
    "l_mm": (5.0, 1000.0),
    "gear": (1.0, 300.0),
    "speed_noload_rpm": (1.0, 20000.0),
    "tau_peak_Nm": (0.1, 5000.0),
    "tau_rated_Nm": (0.05, 5000.0),
    "rotor_inertia_kgm2": (1e-9, 0.1),
    "armature_kgm2": (1e-9, 100.0),
    "l_phase_uh": (1.0, 20000.0),
    "r_phase_ohm": (1e-4, 100.0),
    "kt_Nm_per_A": (0.001, 100.0),
    "i_peak_A": (0.1, 2000.0),
    "voltage_V": (1.0, 1000.0),
    "npu_tops": (0.1, 5000.0),
    "power_max_w": (0.1, 5000.0),
    "current_loop_khz": (0.1, 200.0),
    "bits": (1.0, 32.0),
    "dof": (1.0, 100.0),
    "payload_kg": (0.01, 1000.0),
    "speed_max_mps": (0.01, 30.0),
    "climb_height_mm": (10.0, 2000.0),
    "climb_angle_deg": (1.0, 90.0),
}


def load(name: str) -> list[dict]:
    p = DATA / name
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))


def load_path(p: pathlib.Path) -> list[dict]:
    """按路径读 —— catalog/ 下是按厂商分文件的，不能只按文件名找。"""
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="warning 也算失败")
    args = ap.parse_args()

    # 数据源分两套：catalog/<品类>/<厂商>.json（人工维护）与旧扁平文件（兼容）。
    # 优先校验 catalog/；没有才退回扁平文件。
    cat_dir = DATA / "catalog"
    catalog_files = sorted(cat_dir.glob("*/*.json")) if cat_dir.exists() else []
    files = ([p for p in catalog_files]
             or [DATA / f for f in ("motors.json", "controllers_high.json",
                                    "controllers_low.json", "sensors.json")
                 if (DATA / f).exists()])
    offer_dir = DATA / "offers"
    offer_files = (sorted(offer_dir.glob("*.json")) if offer_dir.exists()
                   else ([DATA / "offers.json"] if (DATA / "offers.json").exists() else []))
    errors: list[str] = []
    warns: list[str] = []
    seen_ids: dict[str, str] = {}
    rows_by_subtype: dict[str, set[str]] = {}

    for p in files:
        fn = p.name
        rows = load_path(p)
        if not rows:
            warns.append(f"{fn}: 空或不存在")
            continue

        for r in rows:
            rid = r.get("id")
            where = f"{fn}:{rid or r.get('model') or '?'}"

            if not rid:
                errors.append(f"{fn}: 有一行没有 id")
                continue
            if rid in seen_ids:
                errors.append(f"{where}: id 重复（已在 {seen_ids[rid]} 出现）")
            seen_ids[rid] = fn

            for k in ("category", "subtype", "vendor", "model", "title"):
                if not r.get(k):
                    errors.append(f"{where}: 缺 {k}")

            tier = r.get("source_tier")
            if tier not in TIERS:
                errors.append(f"{where}: source_tier={tier!r} 不在 {sorted(TIERS)}")
            if "verified" not in r:
                errors.append(f"{where}: 缺 verified 字段（必须显式给 0/1）")

            specs = r.get("specs")
            if not isinstance(specs, dict):
                errors.append(f"{where}: specs 不是对象")
                continue

            # 键集同构：只对**人工逐项核对的 A 级**行要求完全一致
            # （A 级的承诺就是「这一行字段齐、缺的也是确认过的 null」）。
            # 归档导入的 B 级行字段天然参差，只要求 UI 会读的那些键存在，
            # 否则一导入就成了 1000 多条「键集不一致」，把真问题淹掉。
            key = f'{r.get("category")}/{r.get("subtype")}'
            ks = set(specs)
            if r.get("source_tier") == "A":
                if key in rows_by_subtype:
                    if ks != rows_by_subtype[key]:
                        only_here = sorted(ks - rows_by_subtype[key])
                        missing = sorted(rows_by_subtype[key] - ks)
                        errors.append(
                            f"{where}: A 级行键集与同类不一致（多 {only_here}，缺 {missing}）")
                else:
                    rows_by_subtype[key] = ks
            else:
                need = UI_KEYS.get(r.get("category"), set())
                missing_ui = sorted(need - ks)
                if missing_ui:
                    warns.append(f"{where}: 缺 UI 读取的键 {missing_ui}（值可为 null）")

            unknown = sorted(ks - KNOWN_SPEC_KEYS)
            if unknown:
                warns.append(f"{where}: 未登记的参数名 {unknown}（词表可能漂移）")

            # 物理量程：超出去基本是单位/解析 bug
            for name, (lo, hi) in PLAUSIBLE.items():
                v = specs.get(name)
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    if v < lo or v > hi:
                        errors.append(
                            f"{where}: {name}={v:g} 超出物理量程 [{lo:g}, {hi:g}]"
                            f" —— 检查单位换算")

            if r.get("category") == "actuator":
                tau_p = specs.get("tau_peak_Nm")
                tau_r = specs.get("tau_rated_Nm")
                basis = specs.get("tau_basis")
                mass = specs.get("mass_kg")
                ib = specs.get("inertia_basis")
                j = specs.get("rotor_inertia_kgm2")
                arm = specs.get("armature_kgm2")
                gear = specs.get("gear")

                # 执行器至少要有一个可比的扭矩值：峰值、额定，或**堵转**。
                # 只要求峰值，会把「厂商只公布额定」的件拒之门外（GM6020、M2006 就是）；
                # 而为了过闸门去编一个峰值，才是真正的错。
                # 堵转单列（tau_stall_Nm）：它是「锁住转子测的极限」，与峰值同量级
                # 但不是同一个量，所以既不允许它冒充峰值，也不因为它存在就拒收。
                stall = specs.get("tau_stall_Nm")
                if tau_p is None and tau_r is None and stall is None:
                    errors.append(
                        f"{where}: 执行器 tau_peak / tau_rated / tau_stall 都没有")
                elif tau_p is None and tau_r is None:
                    warns.append(f"{where}: 只公布堵转扭矩 {stall} N·m，峰值与额定都缺"
                                 f"（选型时按堵转当上限，别看均分）")
                elif tau_p is None:
                    warns.append(f"{where}: 只公布额定扭矩 {tau_r} N·m，峰值缺失"
                                    f"（跨件按峰值排序时会排最后，这是真话不是惩罚）")
                # tau_basis 只在有峰值时才需要；只有额定/堵转时留 null 是正确状态
                if tau_p is not None and basis not in TAU_BASIS:
                    errors.append(f"{where}: 有峰值但 tau_basis={basis!r} 不在 {sorted(TAU_BASIS)}")
                elif tau_p is None and basis is not None:
                    warns.append(f"{where}: 没有峰值却写了 tau_basis={basis!r}，容易误读")
                if ib is not None and ib not in INERTIA_BASIS:
                    errors.append(f"{where}: inertia_basis={ib!r} 不在 {sorted(INERTIA_BASIS)}")
                if (j is None) != (ib is None):
                    errors.append(f"{where}: rotor_inertia 与 inertia_basis 必须同时给或同时为空")

                # armature = N²·J 的复算校验（读错 kind 会差 10⁴ 倍）
                if j and gear and arm:
                    expect = j * gear ** 2
                    if abs(arm - expect) > 1e-9 * max(1.0, abs(expect)):
                        errors.append(
                            f"{where}: armature={arm:.6g} 与 N²·J={expect:.6g} 不符"
                            f"（差 {arm/expect:.4g}×）—— 检查 inertia_basis")
                if arm is not None and arm <= 0:
                    errors.append(f"{where}: armature 必须为正")

                if tau_p and mass:
                    td = tau_p / mass
                    if td > TD_ABSURD:
                        warns.append(f"{where}: 峰值扭矩密度 {td:.0f} N·m/kg > {TD_ABSURD:.0f}"
                                     f"（RoboParts RL-01：几乎不可信，复核分子/分母口径）")
                    elif td > TD_REVIEW:
                        warns.append(f"{where}: 峰值扭矩密度 {td:.0f} N·m/kg > {TD_REVIEW:.0f} 需复核")
                if tau_p and tau_r:
                    pr = tau_p / tau_r
                    if pr > PR_ABSURD:
                        warns.append(f"{where}: 峰值/额定 {pr:.1f} > {PR_ABSURD:.0f}"
                                     f"（RL-02：基本是瞬时堵转值）")
                    elif pr > PR_REVIEW:
                        warns.append(f"{where}: 峰值/额定 {pr:.1f} > {PR_REVIEW:.0f}"
                                     f"（RL-02：需给持续时间与初始温度）")
                if specs.get("frictionloss_Nm") is None and tau_p:
                    pass  # 允许为空；不吵

    # 优惠：另一套结构，单独校验（data/offers/*.json 或旧的 data/offers.json）
    KINDS = {"sponsor", "coupon", "discount", "giveaway", "event", "edu", "retail"}
    n_offer = 0
    for p in offer_files:
        for r in load_path(p):
            n_offer += 1
            oid = r.get("id")
            where = f"{p.name}:{oid or '?'}"
            if not oid:
                errors.append(f"{p.name}: 有一条没有 id")
            for k in ("kind", "title", "detail"):
                if not r.get(k):
                    errors.append(f"{where}: 缺 {k}")
            if r.get("kind") not in KINDS:
                errors.append(f"{where}: kind={r.get('kind')!r} 未知")
            if "demo" not in r:
                errors.append(f"{where}: 必须显式标 demo: true/false")
            # 只给价格/折扣不给条件 —— 读者会拿它当到手价
            if (r.get("price_cny") is not None or r.get("discount") is not None) \
                    and not r.get("detail"):
                errors.append(f"{where}: 有价格/折扣但没有 detail（获取条件）")
            if r.get("part_id") and r["part_id"] not in seen_ids:
                errors.append(f"{where}: part_id 不在目录里（{r['part_id']}）")
            if r.get("discount") is not None and not (0 < float(r["discount"]) < 1):
                errors.append(f"{where}: discount 应为 0–1 之间的小数")
    if n_offer:
        print(f"优惠 {n_offer} 条（{len(offer_files)} 个文件）")
    else:
        warns.append("offers: 没有优惠数据")

    # 覆盖率报表
    motors = [r for r in (load_path(f) for f in files) if True]
    act = [r for rows in motors for r in rows if r.get("category") == "actuator"]
    if act:
        n = len(act)
        with_arm = sum(1 for r in act if r["specs"].get("armature_kgm2") is not None)
        with_rated = sum(1 for r in act if r["specs"].get("tau_rated_Nm") is not None)
        with_kt = sum(1 for r in act if r["specs"].get("kt_Nm_per_A") is not None)
        with_price = sum(1 for r in act if r.get("price_cny") is not None)
        with_img = sum(1 for r in act if r["specs"].get("image_url"))
        print(f"覆盖率  执行器 {n} 行："
              f"armature {with_arm} ({with_arm/n:.0%}) · "
              f"额定扭矩 {with_rated} ({with_rated/n:.0%}) · "
              f"Kt {with_kt} ({with_kt/n:.0%}) · "
              f"价格 {with_price} ({with_price/n:.0%}) · "
              f"产品图 {with_img} ({with_img/n:.0%})")
        if with_arm / n < 0.5:
            warns.append(f"armature 覆盖率只有 {with_arm/n:.0%}（仿真可用性偏低）")

    print(f"检查了 {len(seen_ids)} 个实体 / {len(rows_by_subtype)} 个 subtype")
    for w in warns:
        print(f"  warn  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    if errors or (args.strict and warns):
        print(f"\n失败：{len(errors)} 个错误、{len(warns)} 个警告")
        return 1
    print(f"\n通过（{len(warns)} 个警告）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
