---
title: Luxonis OAK-D Pro
---


# Luxonis OAK-D Pro

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/luxonis-oak-d-pro.jpg" alt="OAK-D Pro" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">深度相机</span>
      <span class="part-tag sub">深度相机</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag">¥3,060</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 深度量程 (m) | 0.7–12 |
| 视场角 (FOV) | 80°×55° |
| 帧率 (fps) | 120 |
| 分辨率 | 深度 1280×800；RGB 4056×3040 |
| 接口 | USB-C（USB2 / USB3） |
| 额定电压 (V) | 5 |
| 功耗 (W) | 3.5 |
| 防护等级 | IP66 |
| 重量 (g) | 91 |
| 尺寸 (mm) | 97×29.5×22.9 |

<div class="part-src">
来源：<a href="https://shop.luxonis.com/products/oak-d-pro">https://shop.luxonis.com/products/oak-d-pro</a><br/>
收录：Luxonis 官方商城 OAK-D Pro 页面 + OakChina 产品规格页核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="sens-luxonis-oak-d-pro" />
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
| 接口 | USB-C（USB2 / USB3） |
| 噪声 | — |
| 分辨率 | 深度 1280×800；RGB 4056×3040 |
| 深度量程 (m) | 0.7–12 |
| 帧率 (fps) | 120 |
| 视场角 (FOV) | 80°×55° |
| 量程 (m) | — |
| 点频 (pts/s) | — |
| 线数 / 通道 | — |
| 位宽 (bit) | — |
| 精度 / 绝对式 | <2% @<4 m |
| 工作温度 (°C) | -20~50 |
| 尺寸 (mm) | 97×29.5×22.9 |
| 重量 (g) | 91 |
| 功耗 (W) | 3.5 |
| 额定电压 (V) | 5 |
| 防护等级 | IP66 |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://shop.luxonis.com/products/oak-d-pro" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://docs.luxonis.com/" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/luxonis/depthai" target="_blank" rel="noopener">开源项目</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>Luxonis 官方商城 OAK-D Pro 产品图</td></tr><tr><td class="rs-plain">收录说明</td><td>Luxonis 官方商城 OAK-D Pro 页面 + OakChina 产品规格页核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Luxonis+OAK-D+Pro+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=OAK-D+Pro&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Luxonis+OAK-D+Pro+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

主动双目 + IR 点阵/补光，深度在板载 RVC2 上直接算，主机只收结果，适合算力紧张的机上方案。官方推荐 0.7–12 m（800P 最小 0.7 m，扩展模式可到约 0.2 m；理论最远 35 m）；深度 1280×800@120 fps，RGB 12MP@60 fps（IMX378）；IMU 为 BNO086 或 BMI270（分批）。官方 $429（2026-10），按 7.15 汇率约 ¥3060。Waveshare 标的 0.2–9 m 是不同测试口径，与官方推荐值不一致。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
