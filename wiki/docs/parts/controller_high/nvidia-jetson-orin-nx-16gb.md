---
title: 英伟达 NVIDIA Jetson Orin NX 16GB
---


# 英伟达 NVIDIA Jetson Orin NX 16GB

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/jetson-orin-nx-16gb.jpg" alt="Jetson Orin NX 16GB" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">上位机</span>
      <span class="part-tag sub">som</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag muted">无公开报价</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| SoC | Tegra Orin (Orin NX 16GB) |
| CPU | 8× Cortex-A78AE @1.98GHz |
| CUDA 核 | 1024 |
| NPU (TOPS) | 100 |
| 内存 (GB) | 16 |
| 峰值功耗 (W) | 25 |
| 网口 | — |
| CAN 路数 | — |

<div class="part-src">
来源：<a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/">https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/</a><br/>
收录：NVIDIA 官网 Jetson Orin 页面规格表 + 官方价格页核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-nvidia-jetson-orin-nx-16gb" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **算力口径** —— 100 TOPS 通常是 INT8。跑 FP16 的视觉模型按 1/2 估，跑 Transformer 策略还要再打折。
- **内存是硬门槛** —— 16 GB 要同时装相机流、点云和策略。做视觉重的方案直接看 16 GB 档。
- **功耗与散热** —— 峰值 25 W。整机电池与线束要按这个数留余量，别按典型功耗选。



## 全部参数

| 字段 | 值 |
|---|---|
| SoC | Tegra Orin (Orin NX 16GB) |
| CPU | 8× Cortex-A78AE @1.98GHz |
| 核心数 | 8 |
| 架构 | arm64 |
| gpu | 1024-core Ampere + 32 Tensor Cores |
| CUDA 核 | 1024 |
| NPU (TOPS) | 100 |
| 内存 (GB) | 16 |
| 内存带宽 (GB/s) | 102.4 |
| 板载存储 (GB) | — |
| 待机功耗 (W) | — |
| 峰值功耗 (W) | 25 |
| 系统 | JetPack 6 (Ubuntu 22.04) |
| CUDA | 是 |
| ROS 2 | 是 |
| 网口 | — |
| USB | — |
| CAN 路数 | — |
| CSI 相机口 | — |
| PCIe / M.2 | 1× PCIe Gen4 x4 + 3× PCIe Gen4 x1（载板决定） |
| 尺寸 (mm) | 69.6×45 |
| 重量 (g) | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/NVIDIA/jetson-gpio" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/NVIDIA-AI-IOT/ros2_jetson" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>NVIDIA 官网 Jetson Orin 页面 Jetson Orin NX 模组产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>NVIDIA 官网 Jetson Orin 页面规格表 + 官方价格页核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E8%8B%B1%E4%BC%9F%E8%BE%BE+NVIDIA+Jetson+Orin+NX+16GB+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Jetson+Orin+NX+16GB&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E8%8B%B1%E4%BC%9F%E8%BE%BE+NVIDIA+Jetson+Orin+NX+16GB+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

16GB 模组版（260-pin SO-DIMM），不含载板、散热与存储，接口数量由载板决定。标准 10–25W / 100 TOPS（INT8 稀疏），Super 模式 40W / 157 TOPS；16GB 128-bit LPDDR5 102.4GB/s；69.6×45mm。官方 1KU+ 价 $999（2026-07 涨价后），第三方载板套件约 ¥7099。TOPS 口径与 Orin Nano/RDK 不同，不可直接横比。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
