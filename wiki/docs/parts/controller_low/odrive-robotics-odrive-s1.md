---
title: ODrive Robotics ODrive S1
---


# ODrive Robotics ODrive S1

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/odrive-s1.jpg" alt="ODrive S1" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">下位机</span>
      <span class="part-tag sub">servo_driver</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥1,060</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| MCU | — |
| FOC 轴数 | 1 |
| CAN 路数 | 1 |
| 电流环 (kHz) | — |
| 最高电压 (V) | 50.5 |

<div class="part-src">
来源：<a href="https://shop.odriverobotics.com/products/odrive-s1">https://shop.odriverobotics.com/products/odrive-s1</a><br/>
收录：ODrive 官方文档 + 官方商店价格核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-odrive-s1" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **总线够不够** —— 1 路 CAN。12 个关节 × 1 kHz 反馈，单路 CAN 2.0 会吃紧，优先 FD 或多路分载。



## 全部参数

| 字段 | 值 |
|---|---|
| MCU | — |
| 主频 (MHz) | — |
| RAM (KB) | — |
| Flash (KB) | — |
| FOC 轴数 | 1 |
| CAN-FD | 否 |
| CAN 路数 | 1 |
| 电流环 (kHz) | — |
| 力矩模式 | 是 |
| 额定输入电压 (V) | 24 |
| 最高电压 (V) | 50.5 |
| 上位机通信 | USB / CAN / UART / PWM / STEP-DIR |
| 尺寸 (mm) | 66×50 |
| 重量 (g) | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://shop.odriverobotics.com/products/odrive-s1" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://docs.odriverobotics.com/" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/odriverobotics/ODrive" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/odriverobotics/ODriveHardware" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>ODrive 官方商店 ODrive S1 产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>ODrive 官方文档 + 官方商店价格核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=ODrive+Robotics+ODrive+S1+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=ODrive+S1&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=ODrive+Robotics+ODrive+S1+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

单轴 FOC 驱动器；12–50.5V、持续 40A / 峰值 80A、约 2kW；CAN / USB / UART / PWM / STEP-DIR；板载磁编码器，另支持 SPI/ABZ/RS485/Hall；约 66×50mm；MCU 型号官方未公开。价格 $149（2026-10 官方商店），约 ¥1060。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
