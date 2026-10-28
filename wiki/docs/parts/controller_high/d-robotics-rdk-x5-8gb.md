---
title: 地瓜机器人 D-Robotics RDK X5 8GB
---


# 地瓜机器人 D-Robotics RDK X5 8GB

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/rdk-x5-8gb.jpg" alt="RDK X5 8GB" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">上位机</span>
      <span class="part-tag sub">sbc</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥699</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| SoC | Sunrise 5 |
| CPU | 8× Cortex-A55 @1.5GHz |
| CUDA 核 | — |
| NPU (TOPS) | 10 |
| 内存 (GB) | 8 |
| 峰值功耗 (W) | — |
| 网口 | 1× GbE (PoE) |
| CAN 路数 | 1 |

<div class="part-src">
来源：<a href="https://developer.d-robotics.cc/rdkx5">https://developer.d-robotics.cc/rdkx5</a><br/>
收录：D-Robotics 官网产品页 + 规格表核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="cont-drobotics-rdk-x5-8gb" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **算力口径** —— 10 TOPS 通常是 INT8。跑 FP16 的视觉模型按 1/2 估，跑 Transformer 策略还要再打折。
- **内存是硬门槛** —— 8 GB 要同时装相机流、点云和策略。做视觉重的方案直接看 16 GB 档。



## 全部参数

| 字段 | 值 |
|---|---|
| SoC | Sunrise 5 |
| CPU | 8× Cortex-A55 @1.5GHz |
| 核心数 | 8 |
| 架构 | arm64 |
| gpu | 32 GFLOPS |
| CUDA 核 | — |
| NPU (TOPS) | 10 |
| 内存 (GB) | 8 |
| 内存带宽 (GB/s) | — |
| 板载存储 (GB) | — |
| 待机功耗 (W) | — |
| 峰值功耗 (W) | — |
| 系统 | Ubuntu 22.04 (RDK OS) |
| CUDA | 否 |
| ROS 2 | 是 |
| 网口 | 1× GbE (PoE) |
| USB | 4× USB 3.0 Type-A + 1× USB 2.0 Type-C |
| CAN 路数 | 1 |
| CSI 相机口 | 2 |
| PCIe / M.2 | — |
| 尺寸 (mm) | 85×56 |
| 重量 (g) | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://developer.d-robotics.cc/rdkx5" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/D-Robotics/rdk_model_zoo" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/D-Robotics/hobot_dnn" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>D-Robotics 官网 RDK X5 产品页产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>D-Robotics 官网产品页 + 规格表核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E5%9C%B0%E7%93%9C%E6%9C%BA%E5%99%A8%E4%BA%BA+D-Robotics+RDK+X5+8GB+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=RDK+X5+8GB&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E5%9C%B0%E7%93%9C%E6%9C%BA%E5%99%A8%E4%BA%BA+D-Robotics+RDK+X5+8GB+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

8GB 版。官方规格：Sunrise 5、8×A55@1.5GHz、BPU 10 TOPS、4/8GB LPDDR4、85×56mm、5V/5A 供电、Ubuntu 22.04；板载无 eMMC，系统跑 microSD。接口：1× GbE PoE、1× CAN FD、4× USB3.0、2× MIPI CSI、5× UART、8× PWM。价格：2026-08 官方口径 8GB ¥699（2025 上市价 ¥599），4GB ¥549。NPU 10 TOPS 是 BPU 标称 INT8，与 Jetson 的稀疏 INT8 不可直接横比。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
