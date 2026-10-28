---
title: Arduino Uno Rev3
---


# Arduino Uno Rev3

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/arduino-uno-r3.jpg" alt="Uno Rev3" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">下位机</span>
      <span class="part-tag sub">mcu</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥169</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| MCU | ATmega328P (8-bit AVR) |
| FOC 轴数 | — |
| CAN 路数 | 0 |
| 电流环 (kHz) | — |
| 最高电压 (V) | 12 |

<div class="part-src">
来源：<a href="https://docs.arduino.cc/hardware/uno-rev3/">https://docs.arduino.cc/hardware/uno-rev3/</a><br/>
收录：Arduino 官方文档/商店 Tech Specs + A000066 数据手册 + DFRobot 授权代理页面核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-arduino-uno-r3" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **这块不含 FOC 功率级** —— foc_axes 为空是因为板上没有集成电机驱动，不是漏填。电机要外接电调/驱动器，选型时把电调的价格、体积和散热一起算进去。



## 全部参数

| 字段 | 值 |
|---|---|
| MCU | ATmega328P (8-bit AVR) |
| 主频 (MHz) | 16 |
| RAM (KB) | 2 |
| Flash (KB) | 32 |
| FOC 轴数 | — |
| CAN-FD | 否 |
| CAN 路数 | 0 |
| 电流环 (kHz) | — |
| 力矩模式 | — |
| 额定输入电压 (V) | 5 |
| 最高电压 (V) | 12 |
| 上位机通信 | USB-B (ATmega16U2) / UART / SPI / I2C |
| 尺寸 (mm) | 68.6×53.4 |
| 重量 (g) | 25 |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://docs.arduino.cc/hardware/uno-rev3/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf" target="_blank" rel="noopener">官方 PDF</a></td><td>数据手册 / 使用说明书</td></tr><tr><td><a href="https://github.com/arduino/ArduinoCore-avr" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/arduino/Arduino" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>Arduino 官方商店 Arduino Uno Rev3（A000066）产品主图</td></tr><tr><td class="rs-plain">收录说明</td><td>Arduino 官方文档/商店 Tech Specs + A000066 数据手册 + DFRobot 授权代理页面核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Arduino+Uno+Rev3+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Uno+Rev3&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Arduino+Uno+Rev3+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

ATmega328P 16MHz、32KB Flash（0.5KB 引导）、2KB SRAM、1KB EEPROM；14× 数字 I/O（6× PWM）、6× 模拟输入；5V 工作，VIN 推荐 7–12V（极限 6–20V）；USB-B 接口 + ATmega16U2 USB 转串口；无 CAN（can=0）。参考价：DFRobot（Arduino 官方授权大陆代理）¥169（2026-10）；Arduino 官方商店 €29.30。官方尺寸 68.6×53.4mm、25g（DFRobot 标注 75×55×15mm 为含包装/接口尺寸）。适合教学与低实时性外设控制，不适合做 FOC 主控。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
