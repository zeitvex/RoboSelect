---
title: 意法半导体 ST NUCLEO-F103RB
---


# 意法半导体 ST NUCLEO-F103RB

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/st-nucleo-f103rb.jpg" alt="NUCLEO-F103RB" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">下位机</span>
      <span class="part-tag sub">mcu</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥118</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| MCU | STM32F103RBT6 (Cortex-M3) |
| FOC 轴数 | — |
| CAN 路数 | 1 |
| 电流环 (kHz) | — |
| 最高电压 (V) | 12 |

<div class="part-src">
来源：<a href="https://www.st.com/en/evaluation-tools/nucleo-f103rb.html">https://www.st.com/en/evaluation-tools/nucleo-f103rb.html</a><br/>
收录：ST 官网产品页 + Nucleo-64 数据手册 DB2196（Rev 23, 2026-10）核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-st-nucleo-f103rb" />
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
- **总线够不够** —— 1 路 CAN。12 个关节 × 1 kHz 反馈，单路 CAN 2.0 会吃紧，优先 FD 或多路分载。



## 全部参数

| 字段 | 值 |
|---|---|
| MCU | STM32F103RBT6 (Cortex-M3) |
| 主频 (MHz) | 72 |
| RAM (KB) | 20 |
| Flash (KB) | 128 |
| FOC 轴数 | — |
| CAN-FD | 否 |
| CAN 路数 | 1 |
| 电流环 (kHz) | — |
| 力矩模式 | — |
| 额定输入电压 (V) | 5 |
| 最高电压 (V) | 12 |
| 上位机通信 | USB (ST-LINK VCP) / UART / SPI / I2C / CAN |
| 尺寸 (mm) | — |
| 重量 (g) | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.st.com/en/evaluation-tools/nucleo-f103rb.html" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://www.st.com/resource/en/data_brief/nucleo-f103rb.pdf" target="_blank" rel="noopener">官方 PDF</a></td><td>数据手册 / 使用说明书</td></tr><tr><td><a href="https://github.com/STMicroelectronics/STM32CubeF1" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/stm32duino/Arduino_Core_STM32" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>ST 官网 NUCLEO-F103RB 产品页产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>ST 官网产品页 + Nucleo-64 数据手册 DB2196（Rev 23, 2026-10）核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E6%84%8F%E6%B3%95%E5%8D%8A%E5%AF%BC%E4%BD%93+ST+NUCLEO-F103RB+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=NUCLEO-F103RB&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E6%84%8F%E6%B3%95%E5%8D%8A%E5%AF%BC%E4%BD%93+ST+NUCLEO-F103RB+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

Nucleo-64 扩展板，STM32F103RBT6：Cortex-M3 72MHz、128KB Flash、20KB SRAM；Arduino Uno V3 + ST morpho 双排针；板载 ST-LINK/V2-1（含虚拟串口）；1× CAN 控制器引到 morpho 排针，无板载 CAN 收发器，需外接；5V USB 供电或 7–12V VIN。参考价：立创商城 ¥118.19（2026-10，含税）。适合入门 FOC/电机控制与 RM 类开发板替代方案。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
