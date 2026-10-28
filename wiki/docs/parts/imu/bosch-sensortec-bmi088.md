---
title: Bosch Sensortec BMI088
---


# Bosch Sensortec BMI088

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/bosch-bmi088.jpg" alt="BMI088" class="part-photo" />

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
| 加速度量程 (g) | 24 |
| ODR (Hz) | 2000 |
| 噪声 | 0.014 °/s/√Hz；175 µg/√Hz |
| 接口 | SPI、I²C |
| 额定电压 (V) | 3.3 |
| 功耗 (W) | 0.017 |
| 重量 (g) | — |
| 尺寸 (mm) | 3×4.5×0.95 |

<div class="part-src">
来源：<a href="https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi088/">https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi088/</a><br/>
收录：Bosch Sensortec BMI088 产品页 + BST-BMI088-DS001 数据手册核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="sens-bosch-bmi088" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **ODR 与带宽** —— ODR 2000 Hz。四足触地冲击的主要能量在 100–300 Hz，采样要够但别忘低通。
- **装在哪里** —— 尽量远离电机与减速器，或做温补 —— 四足跑久了 IMU 附近升温会有零偏漂移。



## 全部参数

| 字段 | 值 |
|---|---|
| 陀螺量程 (°/s) | 2000 |
| 加速度量程 (g) | 24 |
| ODR (Hz) | 2000 |
| 噪声 | 0.014 °/s/√Hz；175 µg/√Hz |
| 接口 | SPI、I²C |
| 额定电压 (V) | 3.3 |
| 电压范围 (V) | 2.4–3.6 |
| 功耗 (W) | 0.017 |
| 工作温度 (°C) | -40~85 |
| 尺寸 (mm) | 3×4.5×0.95 |
| 重量 (g) | — |
| 分辨率 | 16-bit |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi088/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmi088-ds001.pdf" target="_blank" rel="noopener">官方 PDF</a></td><td>数据手册 / 使用说明书</td></tr><tr><td class="rs-plain">产品图出处</td><td>Bosch Sensortec BMI088 产品页产品渲染图</td></tr><tr><td class="rs-plain">收录说明</td><td>Bosch Sensortec BMI088 产品页 + BST-BMI088-DS001 数据手册核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Bosch+Sensortec+BMI088+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=BMI088&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Bosch+Sensortec+BMI088+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

6 轴（3 轴陀螺 + 3 轴加速度计），陀螺量程 ±125/250/500/1000/2000 °/s，加速度计量程 ±3/6/12/24 g；ODR 12.5 Hz–2 kHz；VDD 2.4–3.6 V，VDDIO 1.2–3.6 V；全速运行 5.15 mA（按 3.3 V 折算约 0.017 W）。博世官方定位为无人机与机器人应用，四足/人形机器人姿态估计常用。官网未公开单价，价格随渠道与批次波动。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
