---
title: TDK InvenSense ICM-42688-P
---


# TDK InvenSense ICM-42688-P

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/tdk-icm-42688-p.png" alt="ICM-42688-P" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">IMU</span>
      <span class="part-tag sub">IMU 芯片</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag muted">无公开报价</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 陀螺量程 (°/s) | 2000 |
| 加速度量程 (g) | 16 |
| ODR (Hz) | 32000 |
| 噪声 | 2.8 mdps/√Hz；70 µg/√Hz |
| 接口 | I3C、I²C、SPI |
| 额定电压 (V) | 3.3 |
| 功耗 (W) | 3.00e-03 |
| 重量 (g) | — |
| 尺寸 (mm) | 2.5×3×0.91 |

<div class="part-src">
来源：<a href="https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/">https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/</a><br/>
收录：TDK InvenSense ICM-42688-P 产品页 + DS-000347 数据手册核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="sens-tdk-icm-42688-p" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **ODR 与带宽** —— ODR 32000 Hz。四足触地冲击的主要能量在 100–300 Hz，采样要够但别忘低通。
- **装在哪里** —— 尽量远离电机与减速器，或做温补 —— 四足跑久了 IMU 附近升温会有零偏漂移。



## 全部参数

| 字段 | 值 |
|---|---|
| 陀螺量程 (°/s) | 2000 |
| 加速度量程 (g) | 16 |
| ODR (Hz) | 32000 |
| 噪声 | 2.8 mdps/√Hz；70 µg/√Hz |
| 接口 | I3C、I²C、SPI |
| 额定电压 (V) | 3.3 |
| 电压范围 (V) | 1.71–3.6 |
| 功耗 (W) | 3.00e-03 |
| 工作温度 (°C) | -40~85 |
| 尺寸 (mm) | 2.5×3×0.91 |
| 重量 (g) | — |
| 分辨率 | 16-bit |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td class="rs-plain">产品图出处</td><td>TDK InvenSense ICM-42688-P 产品页产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>TDK InvenSense ICM-42688-P 产品页 + DS-000347 数据手册核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=TDK+InvenSense+ICM-42688-P+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=ICM-42688-P&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=TDK+InvenSense+ICM-42688-P+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

6 轴；陀螺量程 ±15.6/31.2/62.5/125/250/500/1000/2000 °/s，加速度计量程 ±2/4/8/16 g；低噪声模式 6 轴电流 0.88 mA（按 3.3 V 折算约 0.003 W）；VDD/VDDIO 1.71–3.6 V；最高 ODR 32 kHz。常用于四足/人形机器人与无人机的高频姿态估计。TDK 数据手册下载需登录账号，doc_pdf 留空；官网未公开单价。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
