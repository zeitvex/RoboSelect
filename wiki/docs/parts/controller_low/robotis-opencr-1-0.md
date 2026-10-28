---
title: ROBOTIS OpenCR 1.0
---


# ROBOTIS OpenCR 1.0

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/robotis-opencr-1-0.png" alt="OpenCR 1.0" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">下位机</span>
      <span class="part-tag sub">mcu</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥1,750</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| MCU | STM32F746ZGT6 (Cortex-M7) |
| FOC 轴数 | — |
| CAN 路数 | 3 |
| 电流环 (kHz) | — |
| 最高电压 (V) | 24 |

<div class="part-src">
来源：<a href="https://emanual.robotis.com/docs/en/parts/controller/opencr10/">https://emanual.robotis.com/docs/en/parts/controller/opencr10/</a><br/>
收录：ROBOTIS e-Manual OpenCR 1.0 + 官方商店价格核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-robotis-opencr-1-0" />
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
- **总线够不够** —— 3 路 CAN。12 个关节 × 1 kHz 反馈，单路 CAN 2.0 会吃紧，优先 FD 或多路分载。



## 全部参数

| 字段 | 值 |
|---|---|
| MCU | STM32F746ZGT6 (Cortex-M7) |
| 主频 (MHz) | 216 |
| RAM (KB) | 320 |
| Flash (KB) | 1024 |
| FOC 轴数 | — |
| CAN-FD | 否 |
| CAN 路数 | 3 |
| 电流环 (kHz) | — |
| 力矩模式 | — |
| 额定输入电压 (V) | 12 |
| 最高电压 (V) | 24 |
| 上位机通信 | USB / UART / CAN / RS485 / SPI / I2C |
| 尺寸 (mm) | 105×75 |
| 重量 (g) | 60 |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://emanual.robotis.com/docs/en/parts/controller/opencr10/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/ROBOTIS-GIT/OpenCR" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/ROBOTIS-GIT/OpenCR-Hardware" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>ROBOTIS 官方商店 OpenCR 1.0 产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>ROBOTIS e-Manual OpenCR 1.0 + 官方商店价格核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=ROBOTIS+OpenCR+1.0+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=OpenCR+1.0&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=ROBOTIS+OpenCR+1.0+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

STM32F746ZGT6（216MHz、1MB Flash、320KB SRAM）；3× CAN、3× UART、RS485、SPI/I2C；5–24V 输入；105×75mm、60g；TurtleBot3 常用主控。注意：这是主控板，不含 FOC 功率级；驱动 Dynamixel 走 TTL/RS485，直流电机需外接驱动器。价格 $247.14（ROBOTIS US 商店，2026-10），约 ¥1750。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
