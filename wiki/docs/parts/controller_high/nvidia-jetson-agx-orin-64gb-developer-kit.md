---
title: 英伟达 NVIDIA Jetson AGX Orin 64GB Developer Kit
---


# 英伟达 NVIDIA Jetson AGX Orin 64GB Developer Kit

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/jetson-agx-orin-64gb.jpg" alt="Jetson AGX Orin 64GB Developer Kit" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">上位机</span>
      <span class="part-tag sub">sbc</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag muted">无公开报价</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| SoC | Tegra Orin (AGX Orin 64GB) |
| CPU | 12× Cortex-A78AE @2.2GHz |
| CUDA 核 | 2048 |
| NPU (TOPS) | 275 |
| 内存 (GB) | 64 |
| 峰值功耗 (W) | 60 |
| 网口 | 1× 10GbE + 1× GbE |
| CAN 路数 | 1 |

<div class="part-src">
来源：<a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-agx-orin/">https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-agx-orin/</a><br/>
收录：NVIDIA 官网 Jetson AGX Orin 规格表 + Jetson AGX Orin Developer Kit User Guide 核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-nvidia-jetson-agx-orin-64gb" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **算力口径** —— 275 TOPS 通常是 INT8。跑 FP16 的视觉模型按 1/2 估，跑 Transformer 策略还要再打折。
- **内存是硬门槛** —— 64 GB 要同时装相机流、点云和策略。做视觉重的方案直接看 16 GB 档。
- **功耗与散热** —— 峰值 60 W。整机电池与线束要按这个数留余量，别按典型功耗选。



## 全部参数

| 字段 | 值 |
|---|---|
| SoC | Tegra Orin (AGX Orin 64GB) |
| CPU | 12× Cortex-A78AE @2.2GHz |
| 核心数 | 12 |
| 架构 | arm64 |
| gpu | 2048-core Ampere + 64 Tensor Cores |
| CUDA 核 | 2048 |
| NPU (TOPS) | 275 |
| 内存 (GB) | 64 |
| 内存带宽 (GB/s) | 204.8 |
| 板载存储 (GB) | 64 |
| 待机功耗 (W) | — |
| 峰值功耗 (W) | 60 |
| 系统 | JetPack 6 (Ubuntu 22.04) |
| CUDA | 是 |
| ROS 2 | 是 |
| 网口 | 1× 10GbE + 1× GbE |
| USB | 2× USB-C 3.2 Gen2 + 2× USB-A 3.2 Gen2 + 2× USB-A 3.2 Gen1 + 1× Micro-USB 2.0 |
| CAN 路数 | 1 |
| CSI 相机口 | 6 |
| PCIe / M.2 | 1× PCIe x16 插槽（x8 通道）+ 1× M.2 M-key + 1× M.2 E-key |
| 尺寸 (mm) | 110×110×71.65 (dev kit) |
| 重量 (g) | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-agx-orin/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://docs.nvidia.com/jetson/agx-orin-devkit/user-guide/latest/index.html" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/dusty-nv/jetson-containers" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>NVIDIA 官网 Jetson AGX Orin 开发者套件产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>NVIDIA 官网 Jetson AGX Orin 规格表 + Jetson AGX Orin Developer Kit User Guide 核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E8%8B%B1%E4%BC%9F%E8%BE%BE+NVIDIA+Jetson+AGX+Orin+64GB+Developer+Kit+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Jetson+AGX+Orin+64GB+Developer+Kit&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E8%8B%B1%E4%BC%9F%E8%BE%BE+NVIDIA+Jetson+AGX+Orin+64GB+Developer+Kit+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

官方开发者套件 = AGX Orin 64GB 模组 + 载板 + 散热；275 TOPS（INT8 稀疏）、2048 CUDA + 64 Tensor Cores、12×A78AE@2.2GHz、64GB 256-bit LPDDR5 204.8GB/s、64GB eMMC 5.1、15–60W 可调；10GbE + GbE、16-lane MIPI CSI（最多 6 路）、40-pin 排针含 1× CAN、PCIe x16 插槽（x8 通道）。110×110×71.65mm。官方定价 $3499（2026-07 由 $1999 上调）；国内渠道含税报价差异大，暂不取人民币公开价。TOPS 口径与 Orin Nano/NX 的稀疏标称不同，跨平台不要直接按 TOPS 比值估性能。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
