---
title: RoboParty ROBOTO 01（RP1）
---


# RoboParty ROBOTO 01（RP1）

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/roboparty-rp1.webp" alt="ROBOTO 01（RP1）" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">机械结构</span>
      <span class="part-tag sub">人形</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag muted">无公开报价</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 自由度 | 24 |
| 质量 (kg) | 39 |
| 负载 (kg) | 3 |
| 最大速度 (m/s) | 4 |
| 尺寸 (mm) | 1350×450×200 |
| 攀爬落差 (mm) | 50 |
| 爬坡角度 (°) | 30 |
| 电池 | 10 Ah |
| 续航 (h) | 3 |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | Wi-Fi 6、蓝牙 5.2、4G；ROS 2 |
| 算力 | NVIDIA Jetson Orin NX（16 GB） |
| 传感器 | 可换头部：运控 / 交互 / 数采 / 感知头；感知头为 Intel D435i 深度相机 + 3D 激光雷达，其余头配单目或双目 RGB 相机 |

<div class="part-src">
来源：<a href="https://roboparty.com/products/RP1">https://roboparty.com/products/RP1</a><br/>
收录：RoboParty 官网 ROBOTO 01（/products/RP1）参数表 + RP1_description URDF 关节数核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="struct-roboparty-roboto01" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **人形的负载是手臂负载** —— 标称 3 kg 通常是单手臂最大负载，随伸展姿态变化；整机搬运能力要看厂商的整机负载口径。
- **自由度决定动作空间** —— 24 个关节。腰、腕、手是选配重点，下单前确认这个版本到底包含哪些自由度。
- **先确认是不是同一版本** —— 同名人形常分标准版与 EDU / 开发版，自由度、算力、手部配置都不同，价格也不同 —— 对比参数前先对齐版本。



## 全部参数

| 字段 | 值 |
|---|---|
| 自由度 | 24 |
| 质量 (kg) | 39 |
| 负载 (kg) | 3 |
| 最大速度 (m/s) | 4 |
| 尺寸 (mm) | 1350×450×200 |
| 攀爬落差 (mm) | 50 |
| 爬坡角度 (°) | 30 |
| 电池 | 10 Ah |
| 续航 (h) | 3 |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | Wi-Fi 6、蓝牙 5.2、4G；ROS 2 |
| 算力 | NVIDIA Jetson Orin NX（16 GB） |
| 传感器 | 可换头部：运控 / 交互 / 数采 / 感知头；感知头为 Intel D435i 深度相机 + 3D 激光雷达，其余头配单目或双目 RGB 相机 |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://roboparty.com/products/RP1" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://roboparty.com/documents/roboto-01" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/Roboparty/RP1_description/tree/master/urdf" target="_blank" rel="noopener">URDF / MJCF 模型</a></td><td>官方 / 社区维护的整机模型，可直接导入 PyBullet、MuJoCo、Isaac</td></tr><tr><td><a href="https://github.com/Roboparty/RP1" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/Roboparty/RP1_description" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>RoboParty 官网 ROBOTO 01（RP1）产品图（assets.roboparty.com/web/images/products/rp1/model-portraits-v1/rp1.webp）</td></tr><tr><td class="rs-plain">收录说明</td><td>RoboParty 官网 ROBOTO 01（/products/RP1）参数表 + RP1_description URDF 关节数核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=RoboParty+ROBOTO+01%EF%BC%88RP1%EF%BC%89+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=ROBOTO+01%EF%BC%88RP1%EF%BC%89&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=RoboParty+ROBOTO+01%EF%BC%88RP1%EF%BC%89+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

官网现以 ROBOTO 01 展示该机型（原型号 RP1，GitHub 仓库仍沿用 RP1 命名），分开源版与开源版 PRO：整机 24 / 30 自由度、约 39 / 41 kg、1350×450×200 mm，行走速度约 4 m/s、爬坡 30°、负载 3 kg，10 Ah 电池续航约 3 h，关节模组 ROMOMO 外径 100 mm、峰值扭矩 160 N·m。本条记开源版；RP1_description 的 URDF 为 24 个转动关节。头部可换为运控 / 交互 / 数采 / 感知四种配置，算力为 Orin NX 16 GB，连接为 Wi-Fi 6 / 蓝牙 5.2 / 4G，软件栈含 ROS 2、SDK 与仿真训练代码。官网未公开整机售价，price_cny 留空。另有独立机型 ROBOTO Origin（23 自由度、1.25 m、34 kg），不在本条内。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
