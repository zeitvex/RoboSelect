---
title: 宇树 Unitree B2
---


# 宇树 Unitree B2

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/unitree-b2.jpg" alt="B2" class="part-photo" />

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
| 质量 (kg) | 60 |
| 负载 (kg) | 40 |
| 最大速度 (m/s) | 6 |
| 尺寸 (mm) | 1098×450×645（站立）；880×460×330（折叠） |
| 攀爬落差 (mm) | 400 |
| 爬坡角度 (°) | 45 |
| 电池 | 45 Ah / 2250 Wh / 58 V |
| 续航 (h) | 4–6 h（综合工况） |
| 额定电压 (V) | 58 |
| 电压范围 (V) | — |
| 接口 | 千兆以太网 ×4、USB 3.0 ×4 |
| 算力 | Intel Core i5 / i7；可选 NVIDIA Jetson Orin NX |
| 传感器 | 3D 激光雷达 ×1、深度相机 ×2、光学相机 ×2 |

<div class="part-src">
来源：<a href="https://www.unitree.com/cn/b2">https://www.unitree.com/cn/b2</a><br/>
收录：宇树官网 B2 产品页参数表核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="struct-unitree-b2" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **负载按行走工况算** —— 本行负载取 40 kg（行走口径）。站立静载可能更高，但跑动、越障要按行走负载规划，别拿静载数当动态能力。
- **续航按最差工况留余量** —— 标称 4–6 h（综合工况）。带载、爬坡、低温都会明显缩短，别把空载续航当成交付指标。
- **腿构型决定越障与受力** —— 全膝式、全肘式、前肘后膝（内膝肘）的关节受力与越障姿态不同；同尺寸同质量也不能直接横比爬坡和续航。
- **爬高与爬坡分开看** —— 最大攀爬落差 400 mm、爬坡 45°。落差考验单腿摆高与关节峰值，爬坡考验持续扭矩与抓地。



## 全部参数

| 字段 | 值 |
|---|---|
| 自由度 | 12 |
| 质量 (kg) | 60 |
| 负载 (kg) | 40 |
| 最大速度 (m/s) | 6 |
| 尺寸 (mm) | 1098×450×645（站立）；880×460×330（折叠） |
| 攀爬落差 (mm) | 400 |
| 爬坡角度 (°) | 45 |
| 电池 | 45 Ah / 2250 Wh / 58 V |
| 续航 (h) | 4–6 h（综合工况） |
| 额定电压 (V) | 58 |
| 电压范围 (V) | — |
| 接口 | 千兆以太网 ×4、USB 3.0 ×4 |
| 算力 | Intel Core i5 / i7；可选 NVIDIA Jetson Orin NX |
| 传感器 | 3D 激光雷达 ×1、深度相机 ×2、光学相机 ×2 |

## 优惠与获取条件

::: warning 优惠需要资格，不是人人都能拿到
下面每条的资格都写明。原价与优惠价并列展示，**不划掉原价** —— 资格不满足时按原价算预算。

1. **无固定优惠价**（原价 — 元）
   - 活动：宇树 RM / RC 参赛队首次购买 买二赠一
   - 资格与条件：RM、RC 参赛队凭参赛证明，首次购买可得「买二赠一」；固定结构图纸可向客服索取下载。各型号是否参加以客服确认为准。
   - 有效期：至 2027-12-31
   - 链接：天猫 Unitree 宇树旗舰店
   - 来源：宇树天猫旗舰店商品页（2026-10-28）
:::

## 资料与链接

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.unitree.com/cn/b2" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://support.unitree.com/main/zh" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/unitreerobotics/unitree_ros/tree/master/robots/b2_description" target="_blank" rel="noopener">URDF / MJCF 模型</a></td><td>官方 / 社区维护的整机模型，可直接导入 PyBullet、MuJoCo、Isaac</td></tr><tr><td><a href="https://github.com/unitreerobotics/unitree_sdk2" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/unitreerobotics/unitree_ros" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>宇树官网 B2 产品页首屏产品图（unitree.com/cn/b2）</td></tr><tr><td class="rs-plain">收录说明</td><td>宇树官网 B2 产品页参数表核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E5%AE%87%E6%A0%91+Unitree+B2+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=B2&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E5%AE%87%E6%A0%91+Unitree+B2+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

工业级四足：12 自由度、整机 60 kg。官网给的是上限口径——站立负载 ≥120 kg、行走负载 >40 kg（payload_kg 取行走值）、速度 >6 m/s（按 6 记录）、爬坡 >45°（按 45 记录）、最大攀爬落差 40 cm、楼梯 20–25 cm。45 Ah / 2250 Wh / 58 V 电池，综合续航 4–6 h；IP67、工作温度 -20~55 ℃。算力可选 i5/i7 与 Orin NX，传感器为 1×3D 激光雷达 + 2×深度相机 + 2×光学相机。官网未公开售价，price_cny 留空。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
