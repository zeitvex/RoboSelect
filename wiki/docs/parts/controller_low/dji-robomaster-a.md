---
title: 大疆 DJI RoboMaster 开发板 A 型
---


# 大疆 DJI RoboMaster 开发板 A 型

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/dji-dev-board-a.jpg" alt="RoboMaster 开发板 A 型" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">下位机</span>
      <span class="part-tag sub">mcu</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥429</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| MCU | STM32F427IIH6 (Cortex-M4) |
| FOC 轴数 | — |
| CAN 路数 | 2 |
| 电流环 (kHz) | — |
| 最高电压 (V) | 26 |

<div class="part-src">
来源：<a href="https://www.robomaster.com/zh-CN/products/components/general/development-board">https://www.robomaster.com/zh-CN/products/components/general/development-board</a><br/>
收录：DJI RoboMaster 官网产品页 + 技术参数核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-dji-dev-board-a" />
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
- **总线够不够** —— 2 路 CAN。12 个关节 × 1 kHz 反馈，单路 CAN 2.0 会吃紧，优先 FD 或多路分载。



## 全部参数

| 字段 | 值 |
|---|---|
| MCU | STM32F427IIH6 (Cortex-M4) |
| 主频 (MHz) | 180 |
| RAM (KB) | 256 |
| Flash (KB) | 2048 |
| FOC 轴数 | — |
| CAN-FD | 否 |
| CAN 路数 | 2 |
| 电流环 (kHz) | — |
| 力矩模式 | — |
| 额定输入电压 (V) | 24 |
| 最高电压 (V) | 26 |
| 上位机通信 | USB / CAN / UART / DBUS |
| 尺寸 (mm) | 85×58 |
| 重量 (g) | 48 |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.robomaster.com/zh-CN/products/components/general/development-board" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/RoboMaster/DevelopmentBoard-Examples" target="_blank" rel="noopener">开源项目</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>DJI RoboMaster 开发板套件页面产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>DJI RoboMaster 官网产品页 + 技术参数核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E5%A4%A7%E7%96%86+DJI+RoboMaster+%E5%BC%80%E5%8F%91%E6%9D%BF+A+%E5%9E%8B+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=RoboMaster+%E5%BC%80%E5%8F%91%E6%9D%BF+A+%E5%9E%8B&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E5%A4%A7%E7%96%86+DJI+RoboMaster+%E5%BC%80%E5%8F%91%E6%9D%BF+A+%E5%9E%8B+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

STM32F427IIH6；CAN1 6 口 / CAN2 4 口、4× UART、蓝牙串口、DBUS、16 路可调 PWM + 4 路无电源 PWM、18× GPIO、IMU + 电子罗盘；26V 上限、4–6S LiPo、持续 20A、85×58mm、48g。注意：这是主控板，不含 FOC 功率级，电机需外接 C620/C610 电调。官方价 ¥429。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
