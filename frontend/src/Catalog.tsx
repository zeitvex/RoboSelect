import { Table, Tag, Skeleton, Empty } from 'antd'
import { DownloadOutlined, SearchOutlined, TableOutlined, AppstoreOutlined } from '@ant-design/icons'
import { useQuery } from '@tanstack/react-query'
import { useEffect, useMemo, useState } from 'react'
import { api, type Part } from './api'
import { F, SENSOR_HERO, fmtField } from './fields'
import PartCard from './components/PartCard'
import { PartDrawer } from './ui'
import { useAuth } from './App'

//: 品类。顺序即展示顺序 —— 关节电机是当前重点，放最前。
//: 机械结构 / 电池 / 线束 目前没有收录：不是漏了，是没有可信来源，
//: 宁可显示「未收录」也不编数（见 README 的口径纪律）。
const CATS = [
  { value: 'actuator', label: '关节电机', hint: '选型主战场' },
  { value: 'controller_high', label: '上位机', hint: '推理与感知' },
  { value: 'controller_low', label: '下位机', hint: '力矩闭环' },
  { value: 'structure', label: '机械结构', hint: '整机形态' },
  { value: 'imu', label: 'IMU', hint: '姿态与振动' },
  { value: 'lidar', label: '激光雷达', hint: '地形与建图' },
  { value: 'camera', label: '深度相机', hint: '视觉感知' },
  { value: 'battery', label: '电池', hint: '待收录' },
  { value: 'wiring', label: '线束', hint: '待收录' },
  { value: 'module', label: '其余模块', hint: '力触觉 / 编码器' },
]

const SORTS = [
  { value: 'featured', label: '推荐（有评价优先）' },
  { value: 'vendor', label: '厂商' },
  { value: 'tau_peak', label: '峰值扭矩' },
  { value: 'armature', label: 'armature' },
  { value: 'mass', label: '质量' },
  { value: 'price', label: '价格' },
]

function StatPill({ label, value, suffix }: { label: string; value: any; suffix?: string }) {
  return (
    <div className="rounded-lg border border-slate-200 bg-slate-50 px-3 py-2">
      <div className="text-[10.5px] uppercase tracking-wider text-slate-400">{label}</div>
      <div className="mt-0.5 text-[17px] font-semibold text-slate-900">
        {value ?? '—'}<span className="ml-0.5 text-[11px] font-normal text-slate-400">{suffix}</span>
      </div>
    </div>
  )
}

/** 卡片视图的表格列（仅用于表格切换，保留原有能力） */
function tableColumns(cat: string) {
  const num = (v: any) => <span className="tabular-nums">{v}</span>
  const base = [
    {
      title: '型号', dataIndex: 'model', width: 210, fixed: 'left' as const,
      render: (_: any, r: Part) => (
        <div>
          <div className="font-semibold">{r.model}</div>
          <div className="text-[11.5px] text-slate-500">{r.subtype_label}</div>
        </div>
      ),
    },
    { title: '厂商', dataIndex: 'vendor', width: 130 },
  ]
  if (cat === 'actuator') {
    return [...base,
      { title: '峰值 τ', width: 96, align: 'right' as const, render: (_: any, r: Part) => num(fmtField('tau_peak_Nm', r.specs.tau_peak_Nm) ?? '—') },
      { title: '减速比', width: 88, align: 'right' as const, render: (_: any, r: Part) => num(r.specs.gear ?? '—') },
      { title: '空载 rpm', width: 100, align: 'right' as const, render: (_: any, r: Part) => num(r.specs.speed_noload_rpm ?? '—') },
      { title: '质量 kg', width: 90, align: 'right' as const, render: (_: any, r: Part) => num(r.specs.mass_kg ?? '—') },
      { title: 'armature', width: 112, align: 'right' as const, render: (_: any, r: Part) => r.specs.armature_kgm2 ? <span className="text-blue-600 tabular-nums">{fmtField('armature_kgm2', r.specs.armature_kgm2)}</span> : '—' },
      { title: '价', width: 80, align: 'right' as const, render: (_: any, r: Part) => r.price_cny ? `¥${r.price_cny}` : '—' },
      { title: '评价', width: 70, align: 'right' as const, render: (_: any, r: Part) => r.review_count || '—' },
    ]
  }
  if (cat === 'controller_high') {
    return [...base,
      { title: 'SoC', width: 170, render: (_: any, r: Part) => r.specs.soc ?? '—' },
      { title: 'CUDA', width: 80, align: 'right' as const, render: (_: any, r: Part) => r.specs.cuda_cores ?? '—' },
      { title: 'NPU', width: 90, align: 'right' as const, render: (_: any, r: Part) => r.specs.npu_tops ? `${r.specs.npu_tops} TOPS` : '—' },
      { title: '内存', width: 80, align: 'right' as const, render: (_: any, r: Part) => r.specs.ram_gb ? `${r.specs.ram_gb} GB` : '—' },
      { title: '峰值 W', width: 90, align: 'right' as const, render: (_: any, r: Part) => r.specs.power_max_w ?? '—' },
      { title: '价', width: 84, align: 'right' as const, render: (_: any, r: Part) => r.price_cny ? `¥${r.price_cny}` : '—' },
    ]
  }
  if (cat === 'controller_low') {
    return [...base,
      { title: 'MCU', width: 190, render: (_: any, r: Part) => r.specs.mcu ?? '—' },
      { title: 'FOC', width: 70, align: 'right' as const, render: (_: any, r: Part) => r.specs.foc_axes ?? '—' },
      { title: 'CAN', width: 70, align: 'right' as const, render: (_: any, r: Part) => `${r.specs.can ?? '—'}${r.specs.canfd ? ' FD' : ''}` },
      { title: '电流环', width: 90, align: 'right' as const, render: (_: any, r: Part) => r.specs.current_loop_khz ? `${r.specs.current_loop_khz} kHz` : '—' },
      { title: '最高 V', width: 86, align: 'right' as const, render: (_: any, r: Part) => r.specs.voltage_max_V ?? '—' },
      { title: '价', width: 84, align: 'right' as const, render: (_: any, r: Part) => r.price_cny ? `¥${r.price_cny}` : '—' },
    ]
  }
  if (cat === 'structure') {
    return [...base,
      { title: '自由度', width: 80, align: 'right' as const, render: (_: any, r: Part) => num(r.specs.dof ?? '—') },
      { title: '质量 kg', width: 90, align: 'right' as const, render: (_: any, r: Part) => num(r.specs.mass_kg ?? '—') },
      { title: '负载 kg', width: 90, align: 'right' as const, render: (_: any, r: Part) => num(r.specs.payload_kg ?? '—') },
      { title: '最大速度', width: 100, align: 'right' as const, render: (_: any, r: Part) => r.specs.speed_max_mps ? `${r.specs.speed_max_mps} m/s` : '—' },
      { title: '价', width: 84, align: 'right' as const, render: (_: any, r: Part) => r.price_cny ? `¥${r.price_cny}` : '—' },
    ]
  }
  return [...base,
    { title: '类型', width: 120, render: (_: any, r: Part) => r.subtype_label },
    {
      title: '关键参数', render: (_: any, r: Part) => {
        const fn = SENSOR_HERO[r.subtype]
        return <span className="text-[12.5px] text-slate-500">{fn ? fn(r) : (r.notes || '')}</span>
      },
    },
    { title: '价', width: 84, align: 'right' as const, render: (_: any, r: Part) => r.price_cny ? `¥${r.price_cny}` : '—' },
  ]
}

export default function Catalog({ onOpenPost, onCompose, openAuth }: {
  onOpenPost: (id: number) => void
  onCompose: (partId: string) => void
  openAuth: () => void
}) {
  const { user } = useAuth()
  const [cat, setCat] = useState('actuator')
  const [vendor, setVendor] = useState<string | undefined>()
  const [subtype, setSubtype] = useState<string | undefined>()
  const [q, setQ] = useState('')
  const [sort, setSort] = useState('featured')
  const [order, setOrder] = useState<'asc' | 'desc'>('asc')
  const [page, setPage] = useState(1)
  const [pageSize, setPageSize] = useState(24)
  const [view, setView] = useState<'grid' | 'table'>('grid')
  const [openId, setOpenId] = useState<string | null>(null)
  const [filtersOpen, setFiltersOpen] = useState(false)

  const catalog = useQuery({ queryKey: ['catalog', cat], queryFn: () => api.catalog(cat) })
  const stats = useQuery({ queryKey: ['stats'], queryFn: api.stats })
  const query = useMemo(() => ({
    category: cat, vendor, subtype, q, sort, order, limit: pageSize,
    offset: (page - 1) * pageSize,
  }), [cat, vendor, subtype, q, sort, order, page, pageSize])
  const parts = useQuery({ queryKey: ['parts', query], queryFn: () => api.parts(query) })

  useEffect(() => { setPage(1) }, [cat, vendor, subtype, q, sort, order])
  useEffect(() => { setVendor(undefined); setSubtype(undefined) }, [cat])

  const catCount = (v: string) =>
    (catalog.data?.facets || []).filter((f: any) => f.category === v)
      .reduce((sum: number, f: any) => sum + f.n, 0)

  const total = parts.data?.total ?? 0
  const pages = Math.max(1, Math.ceil(total / pageSize))
  const items = parts.data?.items ?? []

  return (
    <div>
      {/* 顶部：标题 + 分段统计条（VS Code 风的「一块白卡里分格」） */}
      <div className="mb-5 flex flex-wrap items-end justify-between gap-4">
        <div>
          <h1 className="title-gradient text-[26px] font-extrabold leading-tight tracking-tight">
            四足机器人 · 部件选型
          </h1>
          <p className="mt-1.5 max-w-xl text-[12.5px] leading-relaxed text-slate-500">
            每个参数都带口径与来源；关节电机额外标出仿真要用的 <code>armature</code>。
            卡片下方是<strong className="text-slate-600">最高赞的实测评价</strong>。
          </p>
        </div>
        <div className="flex overflow-hidden rounded-lg border border-slate-200 bg-white
                        shadow-[0_1px_2px_rgba(0,0,0,0.06)]">
          {[
            { label: '零件', v: stats.data?.parts, s: '件' },
            { label: '有 armature', v: stats.data?.with_armature, s: '件' },
            { label: '社区成员', v: stats.data?.users, s: '人' },
            { label: '讨论评价', v: stats.data?.posts, s: '条' },
          ].map((c, i) => (
            <div key={c.label}
              className={`px-4 py-2.5 ${i ? 'border-l border-slate-200' : ''}`}>
              <div className="text-[19px] font-bold leading-none text-blue-600 tabular">
                {c.v ?? '—'}<span className="ml-0.5 text-[11px] font-normal text-slate-400">{c.s}</span>
              </div>
              <div className="mt-1 text-[11px] text-slate-500">{c.label}</div>
            </div>
          ))}
        </div>
      </div>

      {/* 分类：药丸，选中 = 实心蓝；空品类灰掉并说明原因 */}
      <div className="mb-3 flex flex-wrap items-center gap-1.5">
        {CATS.map(c => {
          const on = c.value === cat
          const n = catCount(c.value)
          return (
            <button key={c.value} onClick={() => setCat(c.value)}
              title={n ? `${c.label} · ${n} 件 · ${c.hint}` : `${c.label}：还没有收录（没有可信来源，不编数据）`}
              className={`rounded-full border px-3.5 py-[7px] text-[13px] transition
                ${on
                  ? 'border-blue-600 bg-blue-600 font-semibold text-white'
                  : n
                    ? 'border-slate-200 bg-[var(--surface)] text-slate-600 hover:border-slate-300 hover:text-slate-900'
                    : 'border-dashed border-slate-200 bg-transparent text-slate-400 hover:border-slate-300'}`}>
              {c.label}
              <span className={`ml-1.5 text-[11px] ${on ? 'text-blue-100' : 'text-slate-400'}`}>
                {n || '未收录'}
              </span>
            </button>
          )
        })}
      </div>

      {/* 工具栏 */}
      <div className="mb-4 flex flex-wrap items-center gap-2">
        <div className="relative">
          <SearchOutlined className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            value={q} onChange={e => setQ(e.target.value)}
            placeholder="搜型号 / 厂商 / 通信方式"
            className="w-[240px] rounded-full border border-slate-200 bg-[var(--surface)] py-2 pl-9 pr-3
                       text-[13px] text-slate-900 placeholder:text-slate-400
                       outline-none transition focus:border-blue-600"
          />
        </div>

        <button onClick={() => setFiltersOpen(v => !v)}
          className={`rounded-full border px-3.5 py-2 text-[12.5px] transition
            ${vendor || subtype || filtersOpen
              ? 'border-blue-600 bg-blue-50 font-medium text-blue-600'
              : 'border-slate-200 bg-[var(--surface)] text-slate-600 hover:border-slate-300'}`}>
          筛选{(vendor ? ' · 1' : '')}{(subtype ? ' · 1' : '')}
        </button>

        <select value={sort} onChange={e => setSort(e.target.value)}
          className="rounded-full border border-slate-200 bg-[var(--surface)] px-3 py-2 text-[12.5px]
                     text-slate-700 outline-none focus:border-blue-300">
          {SORTS.map(s => <option key={s.value} value={s.value} className="bg-[var(--surface)]">按{s.label}</option>)}
        </select>
        <button onClick={() => setOrder(o => o === 'asc' ? 'desc' : 'asc')}
          className="rounded-full border border-slate-200 bg-[var(--surface)] px-3 py-2 text-[12.5px]
                     text-slate-600 transition hover:border-slate-300">
          {order === 'asc' ? '↑ 升序' : '↓ 降序'}
        </button>

        <div className="ml-auto flex items-center gap-1.5">
          <span className="mr-1 text-[12px] text-slate-400">
            {total} 项{total > pageSize && ` · 第 ${page}/${pages} 页`}
          </span>
          <button onClick={() => setView(v => v === 'grid' ? 'table' : 'grid')}
            className="rounded-full border border-slate-200 bg-[var(--surface)] p-2 text-slate-500
                       transition hover:border-slate-300 hover:text-slate-800"
            title={view === 'grid' ? '切到表格' : '切到卡片'}>
            {view === 'grid' ? <TableOutlined /> : <AppstoreOutlined />}
          </button>
          <button onClick={async () => {
            const r = await api.exportDraft()
            const blob = new Blob([r.actuators_yaml], { type: 'text/plain;charset=utf-8' })
            const a = document.createElement('a')
            a.href = URL.createObjectURL(blob); a.download = 'roboselect-export.yaml'; a.click()
            URL.revokeObjectURL(a.href)
          }}
            className="rounded-full border border-slate-200 bg-[var(--surface)] px-3 py-2 text-[12.5px]
                       text-slate-600 transition hover:border-slate-300 hover:text-slate-800">
            <DownloadOutlined /> 导出
          </button>
        </div>
      </div>

      {/* 筛选面板 */}
      {filtersOpen && (
        <div className="mb-4 rounded-lg border border-slate-200 bg-slate-50 p-3">
          <div className="mb-2 flex flex-wrap items-center gap-1.5">
            <span className="mr-1 text-[11px] uppercase tracking-wider text-slate-400">厂商</span>
            {(catalog.data?.vendors || []).map(v => {
              const on = vendor === v.vendor
              return (
                <button key={v.vendor}
                  onClick={() => { setVendor(on ? undefined : v.vendor); setPage(1) }}
                  className={`rounded-full px-2.5 py-[3px] text-[11.5px] transition
                    ${on ? 'bg-blue-50 text-blue-600 ring-1 ring-blue-200'
                         : 'bg-slate-100 text-slate-500 hover:text-slate-800'}`}>
                  {v.vendor} <span className="text-slate-400">{v.n}</span>
                </button>
              )
            })}
          </div>
          <div className="flex flex-wrap items-center gap-1.5">
            <span className="mr-1 text-[11px] uppercase tracking-wider text-slate-400">子类</span>
            {(catalog.data?.facets || []).filter(f => f.category === cat).map(s => {
              const on = subtype === s.subtype
              return (
                <button key={s.subtype}
                  onClick={() => { setSubtype(on ? undefined : s.subtype); setPage(1) }}
                  className={`rounded-full px-2.5 py-[3px] text-[11.5px] transition
                    ${on ? 'bg-sky-50 text-sky-700 ring-1 ring-sky-200'
                         : 'bg-slate-100 text-slate-500 hover:text-slate-800'}`}>
                  {s.subtype_label} <span className="text-slate-400">{s.n}</span>
                </button>
              )
            })}
          </div>
        </div>
      )}

      {/* 内容 */}
      {parts.isLoading ? (
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4">
          {Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="h-[300px] animate-pulse rounded-lg border border-slate-200 bg-slate-50" />
          ))}
        </div>
      ) : !items.length ? (
        <Empty description={
          <span className="text-slate-500">
            {catCount(cat)
              ? '没有符合条件的零件'
              : `${CATS.find(c => c.value === cat)?.label} 还没有收录 —— 没有可信来源，宁缺不编`}
          </span>
        } />
      ) : view === 'grid' ? (
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4">
          {items.map(p => <PartCard key={p.id} part={p} onOpen={setOpenId} />)}
        </div>
      ) : (
        <Table
          size="small" rowKey="id" dataSource={items}
          columns={tableColumns(cat) as any}
          scroll={{ x: 1000 }} pagination={false}
          onRow={r => ({ onClick: () => setOpenId(r.id), style: { cursor: 'pointer' } })}
        />
      )}

      {/* 分页 */}
      {pages > 1 && (
        <div className="mt-5 flex items-center justify-center gap-2">
          <button disabled={page === 1} onClick={() => setPage(p => p - 1)}
            className="rounded-full border border-slate-200 bg-[var(--surface)] px-3.5 py-1.5 text-[12.5px]
                       text-slate-600 transition disabled:opacity-30 hover:border-slate-300">
            上一页
          </button>
          <span className="px-2 text-[12.5px] tabular-nums text-slate-500">{page} / {pages}</span>
          <button disabled={page >= pages} onClick={() => setPage(p => p + 1)}
            className="rounded-full border border-slate-200 bg-[var(--surface)] px-3.5 py-1.5 text-[12.5px]
                       text-slate-600 transition disabled:opacity-30 hover:border-slate-300">
            下一页
          </button>
        </div>
      )}

      <PartDrawer partId={openId} open={!!openId} onClose={() => setOpenId(null)}
        onOpenPost={id => { setOpenId(null); onOpenPost(id) }}
        onCompose={partId => { setOpenId(null); if (!user) return openAuth(); onCompose(partId) }} />
    </div>
  )
}
