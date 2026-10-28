---
title: UC Berkeley Hybrid Robotics Berkeley Humanoid Lite
---


# UC Berkeley Hybrid Robotics Berkeley Humanoid Lite

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/berkeley-humanoid-lite.jpg" alt="Berkeley Humanoid Lite" class="part-photo" />

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
| 自由度 | 22 |
| 质量 (kg) | 16 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | 800（高） |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | 6S LiPo（22.2 V） |
| 续航 (h) | ≈0.5 h（6S LiPo） |
| 额定电压 (V) | 22.2 |
| 电压范围 (V) | — |
| 接口 | — |
| 算力 | Intel N95 迷你主机 |
| 传感器 | IMU |

<div class="part-src">
来源：<a href="https://lite.berkeley-humanoid.org/">https://lite.berkeley-humanoid.org/</a><br/>
收录：Berkeley Humanoid Lite 官网 + 官方 GitHub 仓库 + URDF 关节数核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="struct-berkeley-humanoid-lite" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **自由度决定动作空间** —— 22 个关节。腰、腕、手是选配重点，下单前确认这个版本到底包含哪些自由度。
- **先确认是不是同一版本** —— 同名人形常分标准版与 EDU / 开发版，自由度、算力、手部配置都不同，价格也不同 —— 对比参数前先对齐版本。



## 全部参数

| 字段 | 值 |
|---|---|
| 自由度 | 22 |
| 质量 (kg) | 16 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | 800（高） |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | 6S LiPo（22.2 V） |
| 续航 (h) | ≈0.5 h（6S LiPo） |
| 额定电压 (V) | 22.2 |
| 电压范围 (V) | — |
| 接口 | — |
| 算力 | Intel N95 迷你主机 |
| 传感器 | IMU |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://lite.berkeley-humanoid.org/" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/HybridRobotics/Berkeley-Humanoid-Lite-Assets/blob/main/data/robots/berkeley_humanoid/berkeley_humanoid_lite/urdf/berkeley_humanoid_lite.urdf" target="_blank" rel="noopener">URDF / MJCF 模型</a></td><td>官方 / 社区维护的整机模型，可直接导入 PyBullet、MuJoCo、Isaac</td></tr><tr><td><a href="https://github.com/hybridrobotics/berkeley-humanoid-lite" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/HybridRobotics/Berkeley-Humanoid-Lite-Assets" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>Berkeley Humanoid Lite 官网首页封面图（lite.berkeley-humanoid.org）</td></tr><tr><td class="rs-plain">收录说明</td><td>Berkeley Humanoid Lite 官网 + 官方 GitHub 仓库 + URDF 关节数核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=UC+Berkeley+Hybrid+Robotics+Berkeley+Humanoid+Lite+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Berkeley+Humanoid+Lite&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=UC+Berkeley+Hybrid+Robotics+Berkeley+Humanoid+Lite+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

官方开源人形：整机约 16 kg、高 0.8 m、22 自由度（按官方 URDF 关节数），3D 打印摆线针轮执行器，BOM 低于 US$5,000。算力为 Intel N95 迷你主机，6S LiPo 供电续航约 30 min。官网未公布负载、速度、电池容量与对外接口的精确值，相应字段留空；机械 CAD、URDF 与训练资产全部开源。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
