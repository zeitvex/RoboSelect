/** 参数字典：标签、单位、方向。dir: 1=越大越好，-1=越小越好，0=中性不评优。 */

export interface FieldSpec {
  label: string
  unit?: string
  dir?: number
  dec?: number
  sci?: boolean
  bool?: boolean
  enum?: Record<string, string>
  hl?: boolean
}

export const F: Record<string, FieldSpec> = {
  // 执行器
  tau_peak_Nm: { label: '峰值扭矩', unit: 'N·m', dir: 1 },
  tau_rated_Nm: { label: '额定扭矩', unit: 'N·m', dir: 1 },
  tau_basis: { label: '扭矩口径', enum: { peak: '峰值', rated: '额定' } },
  speed_noload_rpm: { label: '空载转速', unit: 'rpm', dir: 1 },
  speed_rated_rpm: { label: '额定转速', unit: 'rpm' },
  gear: { label: '减速比', unit: ':1' },
  mass_kg: { label: '质量', unit: 'kg', dir: -1, dec: 3 },
  od_mm: { label: '直径', unit: 'mm', dir: -1 },
  l_mm: { label: '长度', unit: 'mm', dir: -1 },
  rotor_inertia_kgm2: { label: '转子惯量', unit: 'kg·m²', dir: -1, sci: true },
  inertia_basis: { label: '惯量口径', enum: { rotor: '电机侧转子', output: '输出侧折算' } },
  armature_kgm2: { label: 'armature（反射惯量）', unit: 'kg·m²', sci: true, hl: true },
  voltage_V: { label: '额定电压', unit: 'V' },
  voltage_range_V: { label: '电压范围', unit: 'V' },
  kt_Nm_per_A: { label: '转矩常数 Kt', unit: 'N·m/A' },
  r_phase_ohm: { label: '相电阻', unit: 'Ω', dir: -1 },
  l_phase_uh: { label: '相电感', unit: 'µH' },
  pole_pairs: { label: '极对数' },
  i_rated_A: { label: '额定相电流', unit: 'A' },
  i_peak_A: { label: '峰值相电流', unit: 'A' },
  frictionloss_Nm: { label: '库仑摩擦', unit: 'N·m', dir: -1 },
  damping_Nms_rad: { label: '粘性阻尼', unit: 'N·m·s/rad', dir: -1 },
  encoder: { label: '编码器' },
  comm: { label: '通信' },
  driver_integrated: { label: '集成驱动器', bool: true },
  ip: { label: '防护等级' },
  // 上位机
  soc: { label: 'SoC' },
  cpu: { label: 'CPU' },
  cores: { label: '核心数', dir: 1 },
  cpu_arch: { label: '架构' },
  gpu: { label: 'GPU' },
  cuda_cores: { label: 'CUDA 核', dir: 1 },
  npu_tops: { label: 'NPU 算力', unit: 'TOPS', dir: 1 },
  ram_gb: { label: '内存', unit: 'GB', dir: 1 },
  ram_bw_gbs: { label: '内存带宽', unit: 'GB/s', dir: 1 },
  storage_gb: { label: '存储', unit: 'GB', dir: 1 },
  power_idle_w: { label: '空闲功耗', unit: 'W', dir: -1 },
  power_max_w: { label: '最大功耗', unit: 'W', dir: -1 },
  os: { label: '系统' },
  cuda: { label: 'CUDA', bool: true },
  ros2: { label: 'ROS 2', bool: true },
  eth: { label: '以太网' },
  usb: { label: 'USB' },
  can: { label: 'CAN', unit: '路', dir: 1 },
  csi: { label: 'CSI', unit: '路', dir: 1 },
  pcie: { label: 'PCIe' },
  // 下位机
  mcu: { label: 'MCU' },
  clock_mhz: { label: '主频', unit: 'MHz', dir: 1 },
  ram_kb: { label: 'RAM', unit: 'KB', dir: 1 },
  flash_kb: { label: 'Flash', unit: 'KB', dir: 1 },
  foc_axes: { label: 'FOC 轴数', unit: '轴', dir: 1 },
  canfd: { label: 'CAN-FD', bool: true },
  current_loop_khz: { label: '电流环', unit: 'kHz', dir: 1 },
  torque_mode: { label: '力矩模式', bool: true },
  voltage_in_V: { label: '供电', unit: 'V' },
  voltage_max_V: { label: '最高电压', unit: 'V' },
  comm_upper: { label: '上位通信' },
  // 传感器
  gyro_range_dps: { label: '陀螺量程' },
  accel_range_g: { label: '加速度量程' },
  odr_hz: { label: '输出速率', unit: 'Hz', dir: 1 },
  iface: { label: '接口' },
  noise: { label: '噪声 / 精度' },
  resolution: { label: '分辨率' },
  depth_range_m: { label: '深度范围', unit: 'm' },
  fps: { label: '帧率', unit: 'fps', dir: 1 },
  fov: { label: '视场角' },
  range_m: { label: '量程', unit: 'm', dir: 1 },
  points_per_s: { label: '点频', unit: 'pts/s', dir: 1 },
  channel: { label: '通道' },
  bits: { label: '位数', unit: 'bit', dir: 1 },
  absolute: { label: '绝对式', bool: true },
  temp_range_C: { label: '温度范围' },
  size_mm: { label: '尺寸', unit: 'mm' },
  weight_g: { label: '重量', unit: 'g', dir: -1 },
  // 机械结构（整机形态）
  dof: { label: '自由度', dir: 1 },
  payload_kg: { label: '负载', unit: 'kg', dir: 1 },
  speed_max_mps: { label: '最大速度', unit: 'm/s', dir: 1 },
  climb_height_mm: { label: '攀爬落差', unit: 'mm', dir: 1 },
  climb_angle_deg: { label: '爬坡角度', unit: '°', dir: 1 },
  endurance_h: { label: '续航', unit: 'h', dir: 1 },
  battery: { label: '电池' },
  compute: { label: '算力' },
  sensors: { label: '传感器' },
  price_cny: { label: '参考价', unit: '¥', dir: -1 },
}

export const DERIVED: Record<string, FieldSpec> = {
  torque_density_Nm_per_kg: { label: '扭矩密度', unit: 'N·m/kg', dir: 1, hl: true },
  peak_rated_ratio: { label: '峰值/额定', hl: true },
  speed_noload_rad_s: { label: '空载角速度', unit: 'rad/s', dir: 1 },
  peak_power_W: { label: '峰值功率（τω/4）', unit: 'W', dir: 1 },
  envelope_cm3: { label: '包络体积', unit: 'cm³', dir: -1, dec: 0 },
  armature_check_kgm2: { label: 'armature 复算 N²·J', unit: 'kg·m²', sci: true },
}

/** 一行数值的展示文本；null 返回 null（前端渲染成 —）。 */
export function fmtField(key: string, v: any, spec?: FieldSpec): string | null {
  const s = spec || F[key] || ({} as FieldSpec)
  if (v === null || v === undefined || v === '') return null
  if (s.bool) return v ? '是' : '否'
  if (s.enum) return s.enum[String(v)] ?? String(v)
  if (typeof v === 'number') {
    let txt: string
    if (s.sci) {
      const a = Math.abs(v)
      txt = a !== 0 && (a < 1e-3 || a >= 1e5)
        ? v.toExponential(2)
        : v.toPrecision(4).replace(/\.?0+$/, '')
    } else {
      const dec = s.dec ?? 2
      txt = v.toLocaleString('en-US', { maximumFractionDigits: dec })
    }
    return s.unit === '¥' ? `¥${txt}` : s.unit ? `${txt} ${s.unit}` : txt
  }
  return String(v)
}

export const SENSOR_HERO: Record<string, (p: any) => string> = {
  imu: p => [p.specs.gyro_range_dps && `陀螺 ${p.specs.gyro_range_dps} °/s`,
    p.specs.iface, p.specs.noise].filter(Boolean).join(' · '),
  camera: p => [p.specs.depth_range_m && `${p.specs.depth_range_m} m`,
    p.specs.fov, p.specs.fps && `${p.specs.fps} fps`].filter(Boolean).join(' · '),
  lidar: p => [p.specs.range_m && `${p.specs.range_m} m`, p.specs.fov,
    p.specs.points_per_s && `${Math.round(p.specs.points_per_s / 1000)}k pts/s`]
    .filter(Boolean).join(' · '),
  force: p => [p.specs.channel && `${p.specs.channel} 通道`, p.specs.iface]
    .filter(Boolean).join(' · '),
  encoder: p => [p.specs.bits && `${p.specs.bits} bit`, p.specs.absolute && '绝对式',
    p.specs.iface].filter(Boolean).join(' · '),
}
