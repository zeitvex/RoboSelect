---
title: Stanford Student Robotics Pupper v3
---


# Stanford Student Robotics Pupper v3

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/stanford-pupper.jpg" alt="Pupper v3" class="part-photo" />

  </div>
  <div class="part-hero-right">
    <div class="part-tags">
      <span class="part-tag">机械结构</span>
      <span class="part-tag sub">四足</span>
      <span class="part-tag tierA">来源 A ✓ 已核对</span>
      <span class="part-tag muted">无公开报价</span>
    </div>

<div class="part-split">
<div class="part-official">

#### 官方参数

| 字段 | 值 |
|---|---|
| 自由度 | 12 |
| 质量 (kg) | 3 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | 250×200×220（蹲伏） |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | — |
| 续航 (h) | — |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | — |
| 算力 | Raspberry Pi 5（8 GB） |
| 传感器 | BNO086 IMU、IMX296 222° 鱼眼相机、麦克风 |

<div class="part-src">
来源：<a href="https://github.com/stanfordroboticsclub/StanfordQuadruped">https://github.com/stanfordroboticsclub/StanfordQuadruped</a><br/>
收录：Pupper 官方文档（pupper.readthedocs.io）+ StanfordQuadruped 仓库核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="struct-stanford-pupper-v3" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **腿构型决定越障与受力** —— 全膝式、全肘式、前肘后膝（内膝肘）的关节受力与越障姿态不同；同尺寸同质量也不能直接横比爬坡和续航。



## 全部参数

| 字段 | 值 |
|---|---|
| 自由度 | 12 |
| 质量 (kg) | 3 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | 250×200×220（蹲伏） |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | — |
| 续航 (h) | — |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | — |
| 算力 | Raspberry Pi 5（8 GB） |
| 传感器 | BNO086 IMU、IMX296 222° 鱼眼相机、麦克风 |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://github.com/stanfordroboticsclub/StanfordQuadruped" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://pupper.readthedocs.io/" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td class="rs-plain">产品图出处</td><td>StanfordQuadruped 官方仓库 README 产品图（github.com/stanfordroboticsclub/StanfordQuadruped）</td></tr><tr><td class="rs-plain">收录说明</td><td>Pupper 官方文档（pupper.readthedocs.io）+ StanfordQuadruped 仓库核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Stanford+Student+Robotics+Pupper+v3+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Pupper+v3&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Stanford+Student+Robotics+Pupper+v3+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

12 自由度（每腿 3 个 GIM4305 减速电机，10:1），整机约 3 kg。关节约 3.5 N·m 峰值 / 1.0 N·m 连续（风冷），空载约 30 rad/s；控制器为 Raspberry Pi 5（8 GB），配 BNO086 IMU、IMX296 222° 鱼眼相机、4 英寸 LCD 与 3 W 扬声器，BOM 约 US$2,000。官方仓库没有提供 URDF，urdf_urls 留空；负载、速度、电池与续航官方文档未给，均留空。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
