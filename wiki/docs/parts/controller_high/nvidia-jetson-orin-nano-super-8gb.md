---
title: 英伟达 NVIDIA Jetson Orin Nano Super 8GB
---


# 英伟达 NVIDIA Jetson Orin Nano Super 8GB

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/jetson-orin-nano-super-8gb.jpg" alt="Jetson Orin Nano Super 8GB" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">上位机</span>
      <span class="part-tag sub">sbc</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥1,999</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| SoC | Tegra Orin (Ampere) |
| CPU | 6× Cortex-A78AE @1.7GHz |
| CUDA 核 | 1024 |
| NPU (TOPS) | 67 |
| 内存 (GB) | 8 |
| 峰值功耗 (W) | 25 |
| 网口 | 1× GbE |
| CAN 路数 | 0 |

<div class="part-src">
来源：<a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/">https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/</a><br/>
收录：NVIDIA 官网产品页 + 官方 datasheet PDF 核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-nvidia-jetson-orin-nano-super-8gb" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **算力口径** —— 67 TOPS 通常是 INT8。跑 FP16 的视觉模型按 1/2 估，跑 Transformer 策略还要再打折。
- **内存是硬门槛** —— 8 GB 要同时装相机流、点云和策略。做视觉重的方案直接看 16 GB 档。
- **功耗与散热** —— 峰值 25 W。整机电池与线束要按这个数留余量，别按典型功耗选。



## 全部参数

| 字段 | 值 |
|---|---|
| SoC | Tegra Orin (Ampere) |
| CPU | 6× Cortex-A78AE @1.7GHz |
| 核心数 | 6 |
| 架构 | arm64 |
| gpu | 1024-core Ampere + 32 Tensor Cores |
| CUDA 核 | 1024 |
| NPU (TOPS) | 67 |
| 内存 (GB) | 8 |
| 内存带宽 (GB/s) | 102 |
| 板载存储 (GB) | — |
| 待机功耗 (W) | 7 |
| 峰值功耗 (W) | 25 |
| 系统 | JetPack 6 (Ubuntu 22.04) |
| CUDA | 是 |
| ROS 2 | 是 |
| 网口 | 1× GbE |
| USB | 4× USB 3.2 Gen2 Type-A + 1× USB-C (UFP) |
| CAN 路数 | 0 |
| CSI 相机口 | 2 |
| PCIe / M.2 | 2× M.2 M-key (PCIe 3.0) + 1× M.2 E-key |
| 尺寸 (mm) | 103×90.5×34.8 (dev kit) |
| 重量 (g) | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://dam-cdn.nvd.orangelogic.com/AssetLink/2ug686w80406gxf6q8uv7r3l7265m2n8.pdf" target="_blank" rel="noopener">官方 PDF</a></td><td>数据手册 / 使用说明书</td></tr><tr><td><a href="https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/dusty-nv/jetson-containers" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>NVIDIA 官网 Jetson Orin Nano Super Developer Kit 页面产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>NVIDIA 官网产品页 + 官方 datasheet PDF 核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E8%8B%B1%E4%BC%9F%E8%BE%BE+NVIDIA+Jetson+Orin+Nano+Super+8GB+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Jetson+Orin+Nano+Super+8GB&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E8%8B%B1%E4%BC%9F%E8%BE%BE+NVIDIA+Jetson+Orin+Nano+Super+8GB+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

官方 dev kit：Orin Nano 8GB 模组 + 参考载板。67 TOPS 为稀疏 INT8 标称（1024 CUDA / 32 Tensor），8GB 128-bit LPDDR5 102GB/s，7–25W 可调，103×90.5×34.77mm。无板载存储，需 M.2 NVMe；无原生 CAN。官方定价 $249；国内渠道约 ¥1999。与 RK3588 的 6 TOPS 不是同一计量口径，跨平台不要直接按 TOPS 比值估性能。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
