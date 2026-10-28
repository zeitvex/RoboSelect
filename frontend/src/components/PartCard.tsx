import type { Part } from '../api'
import PartGlyph from './PartGlyph'

/** 科学计数法展示：armature 从 7e-4 到 38 跨五个数量级，固定小数位没法读 */
function sig(v: number): string {
  if (!v) return '0'
  const a = Math.abs(v)
  if (a < 0.01 || a >= 1000) return v.toExponential(2)
  return v.toPrecision(3).replace(/\.?0+$/, '')
}

const SPEC_CHIPS: Record<string, (p: Part) => { k: string; v: string }[]> = {
  actuator: p => {
    const s = p.specs
    const out: { k: string; v: string }[] = []
    if (s.tau_peak_Nm) out.push({ k: '峰值τ', v: `${s.tau_peak_Nm} N·m` })
    if (s.gear) out.push({ k: '减速比', v: `${s.gear}:1` })
    if (s.mass_kg) out.push({ k: '质量', v: `${s.mass_kg} kg` })
    if (s.armature_kgm2) out.push({ k: 'armature', v: sig(s.armature_kgm2) })
    return out.slice(0, 4)
  },
  controller_high: p => {
    const s = p.specs
    const out: { k: string; v: string }[] = []
    if (s.cuda_cores) out.push({ k: 'CUDA', v: String(s.cuda_cores) })
    if (s.npu_tops) out.push({ k: 'NPU', v: `${s.npu_tops} TOPS` })
    if (s.ram_gb) out.push({ k: '内存', v: `${s.ram_gb} GB` })
    if (s.power_max_w) out.push({ k: '峰值', v: `${s.power_max_w} W` })
    return out.slice(0, 4)
  },
  controller_low: p => {
    const s = p.specs
    const out: { k: string; v: string }[] = []
    if (s.mcu) out.push({ k: 'MCU', v: String(s.mcu).replace(/\s*\(.*\)/, '') })
    if (s.can) out.push({ k: 'CAN', v: `${s.can}${s.canfd ? '-FD' : ''}` })
    if (s.current_loop_khz) out.push({ k: '电流环', v: `${s.current_loop_khz} kHz` })
    if (s.foc_axes) out.push({ k: 'FOC', v: `${s.foc_axes} 轴` })
    return out.slice(0, 4)
  },
  sensor: p => {
    const s = p.specs
    const out: { k: string; v: string }[] = []
    if (s.iface) out.push({ k: '接口', v: String(s.iface).split('/')[0] })
    if (s.bits) out.push({ k: '分辨率', v: `${s.bits} bit` })
    if (s.depth_range_m) out.push({ k: '深度', v: `${s.depth_range_m} m` })
    if (s.range_m) out.push({ k: '量程', v: `${s.range_m} m` })
    if (s.fps) out.push({ k: '帧率', v: `${s.fps} fps` })
    if (s.odr_hz) out.push({ k: 'ODR', v: `${s.odr_hz} Hz` })
    return out.slice(0, 4)
  },
  structure: p => {
    const s = p.specs
    const out: { k: string; v: string }[] = []
    if (s.dof) out.push({ k: '自由度', v: String(s.dof) })
    if (s.mass_kg) out.push({ k: '质量', v: `${s.mass_kg} kg` })
    if (s.payload_kg) out.push({ k: '负载', v: `${s.payload_kg} kg` })
    if (s.speed_max_mps) out.push({ k: '速度', v: `${s.speed_max_mps} m/s` })
    return out.slice(0, 4)
  },
}

function Tier({ tier, verified }: { tier: string; verified: boolean }) {
  // VS Code 风的标签：#e6f3ff 底 + 蓝字；B 级降一档用中性灰，C 级用琥珀
  const map: Record<string, string> = {
    A: 'bg-blue-50 text-blue-700 ring-blue-200',
    B: 'bg-slate-50 text-slate-500 ring-slate-200',
    C: 'bg-amber-50 text-amber-700 ring-amber-200',
  }
  return (
    <span className={`rounded-full px-2 py-[3px] text-[10px] font-semibold ring-1 ${map[tier] ?? map.B}`}>
      {tier}
      {verified && ' ✓'}
    </span>
  )
}

function Stars({ v }: { v: number }) {
  return (
    <span className="text-[11px] tracking-tight text-amber-700">
      {'★'.repeat(Math.round(v))}
      <span className="text-slate-300">{'★'.repeat(5 - Math.round(v))}</span>
    </span>
  )
}

export default function PartCard({ part, onOpen }: { part: Part; onOpen: (id: string) => void }) {
  const chips = (SPEC_CHIPS[part.category] ?? (() => []))(part)
  const top = part.top_review

  return (
    <button
      type="button"
      onClick={() => onOpen(part.id)}
      className="group relative flex w-full flex-col overflow-hidden rounded-lg border border-slate-200
                 bg-[var(--surface)] text-left outline-none transition-all duration-200
                 hover:-translate-y-[2px] hover:border-slate-300 hover:shadow-[0_14px_30px_rgba(0,0,0,0.12)]
                 focus-visible:border-slate-300"
    >
      {/* 图片区 */}
      <div
        className="relative flex h-[150px] items-center justify-center overflow-hidden"
        style={{
          background: 'radial-gradient(120% 100% at 50% 0%, var(--plate-bg) 0%, var(--page-bg) 72%)',
        }}
      >
        <div
          className="pointer-events-none absolute inset-0 opacity-70"
          style={{
            backgroundImage:
              'linear-gradient(to right, var(--grid-line) 1px, transparent 1px),'
              + 'linear-gradient(to bottom, var(--grid-line) 1px, transparent 1px)',
            backgroundSize: '22px 22px',
            maskImage: 'radial-gradient(75% 75% at 50% 45%, #000 30%, transparent 100%)',
          }}
        />
        {part.image_url ? (
          /* 真产品照：纯白托板 + multiply 融合。
             厂商图基本是白底 —— 纯白板上 white→white 无缝；换成灰板反而会露出照片
             自己的白边（那圈白边就是照片的底色，不是设计）。暗底照片（如 RS04）保持原样。 */
          <div className="relative mx-3 mb-1 mt-8 flex h-[122px] w-[calc(100%-24px)] items-center
                          justify-center rounded-lg border border-slate-200/80 bg-[var(--photo-plate)] p-2.5
                          shadow-[0_1px_2px_rgba(0,0,0,0.06)]">
            <img src={part.image_url} alt={part.model}
              className="max-h-full max-w-full object-contain transition-transform duration-300 group-hover:scale-[1.04]"
              style={{ mixBlendMode: 'var(--photo-blend)' as any }}
              loading="lazy" />
          </div>
        ) : (
          <div className="relative transition-transform duration-300 group-hover:scale-[1.06]">
            <PartGlyph part={part} size={196} />
          </div>
        )}

        {/* 角标放最上层，避免被产品图挡住 */}
        <div className="absolute right-2.5 top-2.5 z-10 flex items-center gap-1.5">
          {part.rating_avg != null && (
            <span className="rounded-full bg-[var(--surface)]/85 px-2 py-[3px] text-[10px] font-semibold text-amber-600 backdrop-blur">
              ★ {part.rating_avg}
            </span>
          )}
          <span className="rounded-full bg-[var(--surface)]/85 px-1 py-[3px] backdrop-blur">
            <Tier tier={part.source_tier} verified={part.verified} />
          </span>
        </div>

        <span className="absolute left-2.5 top-2.5 z-10 rounded-full bg-[var(--surface)]/85 px-2 py-[3px]
                         text-[10px] text-slate-600 backdrop-blur">
          {part.subtype_label}
        </span>
        {!part.image_url && (
          <span className="absolute bottom-2 right-2.5 z-10 rounded-full bg-[var(--surface)]/80 px-1.5 py-[2px]
                           text-[9.5px] text-slate-400 backdrop-blur"
            title="暂无厂商产品图，此处为按真实 OD/L 尺寸生成的示意图">
            示意图
          </span>
        )}
      </div>

      {/* 文字区 */}
      <div className="flex flex-1 flex-col gap-2 p-3.5">
        <div>
          <div className="truncate text-[14.5px] font-semibold text-slate-900">{part.model}</div>
          <div className="mt-0.5 truncate text-[11.5px] text-slate-500">{part.vendor}</div>
        </div>

        {/* 参数 chip：VS Code 的标签样式（浅蓝底 + 蓝字），数字等宽 */}
        <div className="flex flex-wrap gap-1">
          {chips.map(c => (
            <span key={c.k}
              className="rounded-md bg-blue-50 px-1.5 py-[2px] text-[10.5px] text-blue-700 ring-1 ring-blue-100">
              <span className="text-blue-400">{c.k}</span>{' '}
              <span className="tabular">{c.v}</span>
            </span>
          ))}
        </div>

        {/* 最高赞评价 */}
        <div className="mt-auto min-h-[46px] border-t border-slate-100 pt-2">
          {top ? (
            <div>
              <p className="line-clamp-2 text-[11.5px] leading-[1.5] text-slate-500">
                “{top.excerpt}”
              </p>
              <div className="mt-1 flex items-center gap-1.5 text-[10.5px] text-slate-400">
                <span
                  className="inline-flex h-3.5 w-3.5 items-center justify-center rounded-full text-[8px] text-white"
                  style={{ background: `hsl(212 68% 48%)` }}
                >
                  {top.author?.display_name?.slice(0, 1) ?? '?'}
                </span>
                {top.author?.display_name}
                {top.rating != null && <Stars v={top.rating} />}
                {top.own_hardware && (
                  <span className="rounded bg-blue-50 px-1 text-[9px] text-blue-600">实测</span>
                )}
                <span className="ml-auto text-blue-600">▲ {top.score}</span>
              </div>
            </div>
          ) : (
            <p className="text-[11.5px] text-slate-400">还没有评价 —— 点进去写第一条</p>
          )}
        </div>

        <div className="flex items-center justify-between pt-0.5 text-[11px]">
          <span className="font-medium text-slate-700">
            {part.price_cny ? `¥${part.price_cny.toLocaleString('en-US')}` : <span className="text-slate-400">无报价</span>}
          </span>
          <span className="text-slate-400">{part.review_count || 0} 条评价</span>
        </div>
      </div>
    </button>
  )
}
