---
title: Pollen Robotics Microduck
---


# Pollen Robotics Microduck

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/pollen-microduck.jpg" alt="Microduck" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">机械结构</span>
      <span class="part-tag sub">双足</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag muted">无公开报价</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 自由度 | 14 |
| 质量 (kg) | 0.8 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | 250（高） |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | — |
| 续航 (h) | — |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | USB-C 充电；游戏手柄遥控 |
| 算力 | 板载策略推理，控制频率 50 Hz |
| 传感器 | 相机、激光雷达、双 IMU |

<div class="part-src">
来源：<a href="https://pollen-robotics.com/microduck/">https://pollen-robotics.com/microduck/</a><br/>
收录：Pollen Robotics 官网 Microduck 产品页 + 官方 GitHub 仓库与 MJCF 关节数核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="struct-pollen-microduck" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **整机参数不是部件参数** —— 这一条收的是整机形态，用于对照平台方案；关节电机、主控等部件请到对应品类里选。



## 全部参数

| 字段 | 值 |
|---|---|
| 自由度 | 14 |
| 质量 (kg) | 0.8 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | 250（高） |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | — |
| 续航 (h) | — |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | USB-C 充电；游戏手柄遥控 |
| 算力 | 板载策略推理，控制频率 50 Hz |
| 传感器 | 相机、激光雷达、双 IMU |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://pollen-robotics.com/microduck/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/pollen-robotics/microduck_rl/tree/main/src/mjlab_microduck/robot/microduck" target="_blank" rel="noopener">URDF / MJCF 模型</a></td><td>官方 / 社区维护的整机模型，可直接导入 PyBullet、MuJoCo、Isaac</td></tr><tr><td><a href="https://github.com/pollen-robotics/microduck" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/pollen-robotics/microduck_rl" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>Pollen Robotics 官网 Microduck 页分享图（pollen-robotics.com/assets/og/og-microduck-squad-v2.jpg）</td></tr><tr><td class="rs-plain">收录说明</td><td>Pollen Robotics 官网 Microduck 产品页 + 官方 GitHub 仓库与 MJCF 关节数核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Pollen+Robotics+Microduck+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Microduck&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Pollen+Robotics+Microduck+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

Pollen Robotics 的小型开源双足：14 自由度（每腿 5 + 颈部 1 + 头部 3，按官方 MJCF 执行器数）、约 0.8 kg、高 25 cm，随机附带若干已训练动作，策略在机载 50 Hz 运行，传感器为相机 + 激光雷达 + 双 IMU，配套游戏手柄与 USB-C 充电。官网定价 US$399（2026-10-28 的 introductory price，税前不含运费，可能变化），price_cny 未折算故留空。官方只发布 MuJoCo MJCF（microduck_rl），没有 URDF；负载、速度、电池容量与续航未公开，均留空。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
