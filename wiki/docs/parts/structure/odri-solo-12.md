---
title: ODRI Solo 12
---


# ODRI Solo 12

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/odri-solo12.jpg" alt="Solo 12" class="part-photo" />

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
| 质量 (kg) | 2.5 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | — |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | — |
| 续航 (h) | — |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | 以太网；机身引出供电线（v1 无板载电池） |
| 算力 | Master Board + 12× Micro Driver Board |
| 传感器 | Lord Microstrain 3DM-CX5-25 IMU |

<div class="part-src">
来源：<a href="https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/tree/master/mechanics/quadruped_robot_12dof_v1">https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/tree/master/mechanics/quadruped_robot_12dof_v1</a><br/>
收录：ODRI 官方硬件仓库 README + PAL Robotics Solo12 页面核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="struct-odri-solo12" />
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
| 质量 (kg) | 2.5 |
| 负载 (kg) | — |
| 最大速度 (m/s) | — |
| 尺寸 (mm) | — |
| 攀爬落差 (mm) | — |
| 爬坡角度 (°) | — |
| 电池 | — |
| 续航 (h) | — |
| 额定电压 (V) | — |
| 电压范围 (V) | — |
| 接口 | 以太网；机身引出供电线（v1 无板载电池） |
| 算力 | Master Board + 12× Micro Driver Board |
| 传感器 | Lord Microstrain 3DM-CX5-25 IMU |

## 优惠与获取条件

暂无优惠信息。本站不代理销售，也不收佣金 —— 有合作或团购价请提 issue，写清**价格 + 覆盖范围 + 资格条件 + 有效期**，缺一项都不上卡片。

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/tree/master/mechanics/quadruped_robot_12dof_v1" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://github.com/open-dynamic-robot-initiative/open-dynamic-robot-initiative.github.io/wiki" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/open-dynamic-robot-initiative/robot_properties_solo/tree/master/src/robot_properties_solo/resources/xacro" target="_blank" rel="noopener">URDF / MJCF 模型</a></td><td>官方 / 社区维护的整机模型，可直接导入 PyBullet、MuJoCo、Isaac</td></tr><tr><td><a href="https://github.com/open-dynamic-robot-initiative/robot_properties_solo" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/open-dynamic-robot-initiative/robot_interfaces_solo" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>ODRI 官方硬件仓库 README 产品图（open_robot_actuator_hardware/mechanics/quadruped_robot_12dof_v1）</td></tr><tr><td class="rs-plain">收录说明</td><td>ODRI 官方硬件仓库 README + PAL Robotics Solo12 页面核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=ODRI+Solo+12+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Solo+12&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=ODRI+Solo+12+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

开源力矩控制四足，12 自由度、整机 2.5 kg（官方硬件 README 标注）。v1 没有板载电池与无线通信，需要外接电源和以太网；v1.1 才加板载电池与无线。官方仓库只提供 xacro 模板（solo12.urdf.xacro + leg.xacro），由 robot_properties_solo 生成 URDF，没有预生成文件。官方未公布最高速度、负载、整机尺寸与续航，均留空；PAL Robotics 曾代理整机套件，官网已标注销售停止。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
