---
title: Movella Xsens MTi-3
---


# Movella Xsens MTi-3

<div class="part-hero">
  <div class="part-hero-left">
    
  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">IMU</span>
      <span class="part-tag sub">IMU 模组</span>
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
| ODR (Hz) | 1000 |
| 噪声 | 0.003 °/s/√Hz；70 µg/√Hz |
| 接口 | UART、SPI、I²C |
| 额定电压 (V) | 3.3 |
| 功耗 (W) | 0.1 |
| 重量 (g) | 0.6 |
| 尺寸 (mm) | 12.1×12.1×2.55 |

<div class="part-src">
来源：<a href="https://www.xsens.com/products/sensor-modules/xsens-mti-1-series">https://www.xsens.com/products/sensor-modules/xsens-mti-1-series</a><br/>
收录：Xsens MTi 1-Series 产品页规格表 + xsens_mti_ros_node 官方仓库核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="sens-xsens-mti-3" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **ODR 与带宽** —— ODR 1000 Hz。四足触地冲击的主要能量在 100–300 Hz，采样要够但别忘低通。
- **装在哪里** —— 尽量远离电机与减速器，或做温补 —— 四足跑久了 IMU 附近升温会有零偏漂移。



## 全部参数

| 字段 | 值 |
|---|---|
| 陀螺量程 (°/s) | 2000 |
| 加速度量程 (g) | 16 |
| ODR (Hz) | 1000 |
| 噪声 | 0.003 °/s/√Hz；70 µg/√Hz |
| 接口 | UART、SPI、I²C |
| 额定电压 (V) | 3.3 |
| 电压范围 (V) | 2.8–3.6 |
| 功耗 (W) | 0.1 |
| 工作温度 (°C) | -40~85 |
| 尺寸 (mm) | 12.1×12.1×2.55 |
| 重量 (g) | 0.6 |
| 分辨率 | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.xsens.com/products/sensor-modules/xsens-mti-1-series" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/xsens/xsens_mti_ros_node" target="_blank" rel="noopener">开源项目</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">收录说明</td><td>Xsens MTi 1-Series 产品页规格表 + xsens_mti_ros_node 官方仓库核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Movella+Xsens+MTi-3+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=MTi-3&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Movella+Xsens+MTi-3+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

MTi-1 系列中的 AHRS 型号；陀螺 ±2000 °/s、加速度 ±16 g、磁力 ±8 G；输出频率最高 1 kHz；滚转/俯仰 0.5° RMS，MTi-3 航向 2° RMS；2.8–3.6 V、<100 mW、0.6 g、12.1×12.1×2.55 mm。官网只提供 MTi-3 DK 套件图，未提供独立模组产品图，image_url 留空；价格需向 Movella/Xsens 或代理商询价。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
