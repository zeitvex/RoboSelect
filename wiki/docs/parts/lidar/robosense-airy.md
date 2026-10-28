---
title: RoboSense Airy
---


# RoboSense Airy

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/robosense-airy.jpg" alt="Airy" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">激光雷达</span>
      <span class="part-tag sub">激光雷达</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥4,078</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 量程 (m) | 30 |
| 视场角 (FOV) | 360°×90° |
| 点频 (pts/s) | 1,712,640 |
| 帧率 (fps) | 10 |
| 分辨率 | 0.4°×0.947° |
| 接口 | 100Base-TX 以太网（UDP） |
| 额定电压 (V) | 12 |
| 功耗 (W) | 8 |
| 防护等级 | — |
| 重量 (g) | 240 |
| 尺寸 (mm) | φ60×63 |

<div class="part-src">
来源：<a href="https://www.robosense.ai/rslidar/Airy">https://www.robosense.ai/rslidar/Airy</a><br/>
收录：RoboSense 官网 Airy 产品页 + 产品手册规格页核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="sens-robosense-airy" />
</div>

</div>
  </div>
</div>

::: warning 来源冲突
这份数据的来源之间有分歧，未经覆盖，写在下方「备注」里。
:::

## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **先算视场与量程** —— 近距离抓地形看深度量程下限，别只看最大值；楼梯这类弱纹理场景，结构光/ToF 与双目表现差别很大。



## 全部参数

| 字段 | 值 |
|---|---|
| 陀螺量程 (°/s) | — |
| 加速度量程 (g) | — |
| ODR (Hz) | — |
| 接口 | 100Base-TX 以太网（UDP） |
| 噪声 | — |
| 分辨率 | 0.4°×0.947° |
| 深度量程 (m) | — |
| 帧率 (fps) | 10 |
| 视场角 (FOV) | 360°×90° |
| 量程 (m) | 30 |
| 点频 (pts/s) | 1,712,640 |
| 线数 / 通道 | 96 |
| 位宽 (bit) | — |
| 精度 / 绝对式 | 1 cm @1σ |
| 工作温度 (°C) | — |
| 尺寸 (mm) | φ60×63 |
| 重量 (g) | 240 |
| 功耗 (W) | 8 |
| 额定电压 (V) | 12 |
| 防护等级 | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.robosense.ai/rslidar/Airy" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/RoboSense-LiDAR/rslidar_sdk" target="_blank" rel="noopener">开源项目</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>RoboSense 官网 Airy 产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>RoboSense 官网 Airy 产品页 + 产品手册规格页核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=RoboSense+Airy+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Airy&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=RoboSense+Airy+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

半球形 FOV（360°×90°），30 m@10%、最远 60 m，盲区 0.1 m；96 线，单回波 856,320 pts/s、双回波 1,712,640 pts/s；100 Mbps 以太网 UDP，内置 IMU；9–32 V、<8 W、φ60×63 mm、<240 g。官方页写 1 cm@1σ，产品手册典型值 1.5 cm@1σ——【来源冲突】。官方未公开定价，渠道约 ¥4078（2026-10）；Airy Lite 海外 €600。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
