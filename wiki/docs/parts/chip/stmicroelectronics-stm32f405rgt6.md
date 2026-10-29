---
title: STMicroelectronics STM32F405RGT6
---


# STMicroelectronics STM32F405RGT6

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/chip-st-stm32f405rgt6.png" alt="STM32F405RGT6" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">硬件芯片</span>
      <span class="part-tag soft">mcu</span>
      <span class="part-tag tierB">来源 B</span>
      <span class="part-tag muted">无公开报价</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 主频 (MHz) | 168 |
| 封装 | LQFP64 |
| 额定电压 (V) | 3.3 |
| Flash (KB) | 1024 |
| CAN 路数 | 2 |

<div class="part-src">
来源：<a href="https://www.st.com/en/microcontrollers-microprocessors/stm32f405rg.html">https://www.st.com/en/microcontrollers-microprocessors/stm32f405rg.html</a><br/>
收录：厂商公开资料，未逐项核对到手册页码<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="chip-st-stm32f405rgt6" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **暂无建议** —— 这个型号的关键参数还缺得多，先补齐再谈用法。



## 全部参数

| 字段 | 值 |
|---|---|
| 主频 (MHz) | 168 |
| 封装 | LQFP64 |
| 接口 | — |
| 额定电压 (V) | 3.3 |
| Flash (KB) | 1024 |
| CAN 路数 | 2 |
| cores | 1 |
| RAM (KB) | 192 |
| CAN-FD | 0 |
| doc_url | https://www.st.com/en/microcontrollers-microprocessors/stm32f405rg.html |
| doc_pdf | https://www.st.com/resource/en/datasheet/stm32f405rg.pdf |
| repo_urls | https://github.com/STMicroelectronics/STM32CubeF4 |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 使用者实测

还没有人报过这个件的实测。有的是「参数好看」，缺的是「跑了多久、坏没坏」。

<a class="rt-btn" href="https://github.com/zeitvex/RoboSelect/issues/new?template=review-part.yml&title=%5B%E5%AE%9E%E6%B5%8B%5D+chip-st-stm32f405rgt6&labels=review" target="_blank" rel="noopener">提交实测</a>

需要 GitHub 账号，30 秒填完：装了多大负载、跑了多久、温升多少、坏没坏。
**坏过的经验最值钱** —— 那正是下一个人最想知道的。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.st.com/en/microcontrollers-microprocessors/stm32f405rg.html" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td class="rs-plain">产品图出处</td><td>厂商资料抓取（chip-st-stm32f405rgt6.png）</td></tr><tr><td class="rs-plain">收录说明</td><td>厂商公开资料，未逐项核对到手册页码</td></tr><tr><td><a href="https://www.google.com/search?q=STMicroelectronics+STM32F405RGT6+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=STM32F405RGT6&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=STMicroelectronics+STM32F405RGT6+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr><tr><td><a href="https://github.com/zeitvex/RoboSelect/edit/main/data/catalog/chip/common.json" target="_blank" rel="noopener">在 GitHub 上编辑这条数据</a></td><td>文件 data/catalog/chip/common.json</td></tr></tbody></table>

## 备注

关节驱动器里最常被拿来跑 FOC 的一颗：有 FPU、双 CAN、定时器够多。踩坑点：F405 的 CAN 是 bxCAN（不是 FDCAN），要 CAN FD 得看 G4/H7。



> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
