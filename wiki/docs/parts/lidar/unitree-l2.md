---
title: Unitree L2
---


# Unitree L2

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/unitree-l2.jpg" alt="L2" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">激光雷达</span>
      <span class="part-tag sub">激光雷达</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥1,799</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 量程 (m) | 30 |
| 视场角 (FOV) | 360°×96° |
| 点频 (pts/s) | 64,000 |
| 帧率 (fps) | 10 |
| 分辨率 | — |
| 接口 | 以太网 / 串口 |
| 额定电压 (V) | 12 |
| 功耗 (W) | 10 |
| 防护等级 | — |
| 重量 (g) | 230 |
| 尺寸 (mm) | 75×75×65 |

<div class="part-src">
来源：<a href="https://www.unitree.com/cn/L2">https://www.unitree.com/cn/L2</a><br/>
收录：宇树官网 L2 产品页 + 宇树文档中心核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="sens-unitree-l2" />
</div>

</div>
  </div>
</div>


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
| 接口 | 以太网 / 串口 |
| 噪声 | — |
| 分辨率 | — |
| 深度量程 (m) | — |
| 帧率 (fps) | 10 |
| 视场角 (FOV) | 360°×96° |
| 量程 (m) | 30 |
| 点频 (pts/s) | 64,000 |
| 线数 / 通道 | — |
| 位宽 (bit) | — |
| 精度 / 绝对式 | ±2 cm |
| 工作温度 (°C) | -10~50 |
| 尺寸 (mm) | 75×75×65 |
| 重量 (g) | 230 |
| 功耗 (W) | 10 |
| 额定电压 (V) | 12 |
| 防护等级 | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.unitree.com/cn/L2" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://support.unitree.com/home/zh/developer" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/unitreerobotics/unilidar_sdk2" target="_blank" rel="noopener">开源项目</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>宇树官方商城 L2 产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>宇树官网 L2 产品页 + 宇树文档中心核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Unitree+L2+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=L2&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Unitree+L2+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

非重复扫描，360°×96°，30 m@90%、盲区 0.05 m；有效点频 64,000 pts/s（采样 128,000 pts/s），精度 2 cm；内置 3 轴 IMU，官方提供只用 L2 + IMU 的 Point-LIO 开源 SLAM 方案。10 W（低温自加热峰值 13 W）、12 V、230 g。官网 ¥1799（2026-10），海外 $419。性价比高，但垂直 96° 加上非重复扫描意味着近距离点云比机械式稀，建图算法要适配。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
