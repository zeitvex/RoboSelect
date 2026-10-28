---
title: Manifold Tech Odin1
---


# Manifold Tech Odin1

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/manifold-odin1.webp" alt="Odin1" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">深度相机</span>
      <span class="part-tag sub">深度相机</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥6,199</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 深度量程 (m) | 0.2–30 |
| 视场角 (FOV) | 120°×90° |
| 帧率 (fps) | 15 |
| 分辨率 | 深度 240×180；RGB 1600×1296 |
| 接口 | — |
| 额定电压 (V) | 24 |
| 功耗 (W) | 11 |
| 防护等级 | IP66 |
| 重量 (g) | 280 |
| 尺寸 (mm) | 100×62×43（含航空插头 46） |

<div class="part-src">
来源：<a href="https://www.manifoldtech.cn/products/odin1">https://www.manifoldtech.cn/products/odin1</a><br/>
收录：留形科技官网 Odin1 产品页规格表（逐项读取）+ 下载页核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="sens-manifold-odin1" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **先算视场与量程** —— 近距离抓地形看深度量程下限，别只看最大值；楼梯这类弱纹理场景，结构光/ToF 与双目表现差别很大。



## 全部参数

| 字段 | 值 |
|---|---|
| 陀螺量程 (°/s) | — |
| 加速度量程 (g) | — |
| ODR (Hz) | — |
| 接口 | — |
| 噪声 | — |
| 分辨率 | 深度 240×180；RGB 1600×1296 |
| 深度量程 (m) | 0.2–30 |
| 帧率 (fps) | 15 |
| 视场角 (FOV) | 120°×90° |
| 量程 (m) | — |
| 点频 (pts/s) | 700,000 |
| 线数 / 通道 | — |
| 位宽 (bit) | — |
| 精度 / 绝对式 | ±3 cm @1σ |
| 工作温度 (°C) | -10~40 |
| 尺寸 (mm) | 100×62×43（含航空插头 46） |
| 重量 (g) | 280 |
| 功耗 (W) | 11 |
| 额定电压 (V) | 24 |
| 防护等级 | IP66 |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.manifoldtech.cn/products/odin1" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://www.manifoldtech.cn/download/?product=odin1" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td class="rs-plain">产品图出处</td><td>留形科技官网 Odin1 产品页产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>留形科技官网 Odin1 产品页规格表（逐项读取）+ 下载页核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Manifold+Tech+Odin1+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Odin1&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Manifold+Tech+Odin1+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

官方定位是空间记忆模组而非普通深度相机：SPAD dTOF + 全局快门 RGB + IMU，板载 RK3588 跑 MindSLAM，直接输出彩色点云与位姿。深度 30 m@10% / 70 m@90%（<500 lux），盲区 0.2 m，点频最高 700,000 pts/s；RGB 129°H×104°V；SLAM 定位精度 ±5 cm + 1%。额定 11 W、峰值 24 W，9–26 V 供电，航空插头；物理数据接口以手册为准。价格：京东渠道 ¥6199（2026-10 检索），官方未公开定价；发布时宣传为“千元级”。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
