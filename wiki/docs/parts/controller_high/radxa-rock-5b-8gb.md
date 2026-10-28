---
title: 瑞莎 Radxa ROCK 5B 8GB
---


# 瑞莎 Radxa ROCK 5B 8GB

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/radxa-rock-5b-8gb.webp" alt="ROCK 5B 8GB" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">上位机</span>
      <span class="part-tag sub">sbc</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥884</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| SoC | Rockchip RK3588 |
| CPU | 4× Cortex-A76 @2.4GHz + 4× Cortex-A55 @1.8GHz |
| CUDA 核 | — |
| NPU (TOPS) | 6 |
| 内存 (GB) | 8 |
| 峰值功耗 (W) | — |
| 网口 | 1× 2.5GbE |
| CAN 路数 | 0 |

<div class="part-src">
来源：<a href="https://radxa.com/products/rock5/5b">https://radxa.com/products/rock5/5b</a><br/>
收录：Radxa 官网产品页 + docs.radxa.com 核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-radxa-rock-5b-8gb" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **算力口径** —— 6 TOPS 通常是 INT8。跑 FP16 的视觉模型按 1/2 估，跑 Transformer 策略还要再打折。
- **内存是硬门槛** —— 8 GB 要同时装相机流、点云和策略。做视觉重的方案直接看 16 GB 档。



## 全部参数

| 字段 | 值 |
|---|---|
| SoC | Rockchip RK3588 |
| CPU | 4× Cortex-A76 @2.4GHz + 4× Cortex-A55 @1.8GHz |
| 核心数 | 8 |
| 架构 | arm64 |
| gpu | Mali-G610 MP4 |
| CUDA 核 | — |
| NPU (TOPS) | 6 |
| 内存 (GB) | 8 |
| 内存带宽 (GB/s) | — |
| 板载存储 (GB) | — |
| 待机功耗 (W) | — |
| 峰值功耗 (W) | — |
| 系统 | Radxa OS / Debian / Ubuntu |
| CUDA | 否 |
| ROS 2 | 是 |
| 网口 | 1× 2.5GbE |
| USB | 2× USB 3.0 Type-A + 1× USB 2.0 Type-A + 1× USB-C (PD) |
| CAN 路数 | 0 |
| CSI 相机口 | 1 |
| PCIe / M.2 | 1× M.2 M-key (PCIe 3.0 x4) |
| 尺寸 (mm) | 100×72 |
| 重量 (g) | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://radxa.com/products/rock5/5b" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://docs.radxa.com/en/rock5/rock5b" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/radxa-build/rock-5b" target="_blank" rel="noopener">开源项目</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>Radxa 官网 ROCK 5B 产品图（thumb_rock5b.webp）</td></tr><tr><td class="rs-plain">收录说明</td><td>Radxa 官网产品页 + docs.radxa.com 核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E7%91%9E%E8%8E%8E+Radxa+ROCK+5B+8GB+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=ROCK+5B+8GB&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E7%91%9E%E8%8E%8E+Radxa+ROCK+5B+8GB+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

8GB LPDDR4x 版。RK3588（4×A76@2.4 + 4×A55@1.8）、Mali-G610 MP4、NPU 6 TOPS、2.5GbE、M.2 M-key（PCIe 3.0 x4，支持 NVMe）、USB-C PD、40-pin 扩展口。存储需 eMMC 模块或 microSD，裸板不带。无原生 CAN，需要 CAN 请走 M.2/SPI 扩展。价格：8GB+8GB 存储渠道价约 ¥884（2025-12）；裸板随内存/存储配置浮动。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
