---
title: Stanford Student Robotics Doggo
---


# Stanford Student Robotics Doggo

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/stanford-doggo.jpg" alt="Doggo" class="part-photo" />

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
| 自由度 | 8 |
| 质量 (kg) | 5 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | 420×200×140（机身） |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | — |
| 续航 (h) | — |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | — |
| 算力 | Teensy 3.5 + 4× ODrive |
| 传感器 | — |

<div class="part-src">
来源：<a href="https://github.com/Nate711/StanfordDoggoProject">https://github.com/Nate711/StanfordDoggoProject</a><br/>
收录：Stanford Doggo 官方 GitHub 仓库 + 社区 URDF 关节数核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="struct-stanford-doggo" />
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
| 自由度 | 8 |
| 质量 (kg) | 5 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | 420×200×140（机身） |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | — |
| 续航 (h) | — |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | — |
| 算力 | Teensy 3.5 + 4× ODrive |
| 传感器 | — |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://github.com/Nate711/StanfordDoggoProject" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/RajPShinde/Doggo_Description/tree/master/urdf" target="_blank" rel="noopener">URDF / MJCF 模型</a></td><td>官方 / 社区维护的整机模型，可直接导入 PyBullet、MuJoCo、Isaac</td></tr><tr><td><a href="https://github.com/Nate711/Doggo" target="_blank" rel="noopener">开源项目</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>Stanford Doggo 官方仓库 README 产品图（github.com/Nate711/StanfordDoggoProject/images/hero.jpg）</td></tr><tr><td class="rs-plain">收录说明</td><td>Stanford Doggo 官方 GitHub 仓库 + 社区 URDF 关节数核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=Stanford+Student+Robotics+Doggo+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Doggo&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=Stanford+Student+Robotics+Doggo+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

8 个电机（每腿 2 个）、整机不足 5 kg（按 5 记），BOM 低于 US$3,000，控制器为 Teensy 3.5 + 4× ODrive；腿部五杆机构含被动连杆。社区 URDF（RajPShinde/Doggo_Description）有 20 个可动关节，不能当作驱动自由度。项目官网 doggo.stanford.edu 已无法访问，参数以官方 GitHub 仓库为准；官方未公布负载、速度、电池与续航，均留空。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
