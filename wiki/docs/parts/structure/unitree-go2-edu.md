---
title: 宇树 Unitree Go2 EDU
---


# 宇树 Unitree Go2 EDU

<div class="part-hero">
  <div class="part-hero-left">
    <img src="/parts/unitree-go2-edu.jpg" alt="Go2 EDU" class="part-photo" />

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
| 质量 (kg) | 15 |
| 负载 (kg) | 8 |
| 最大速度 (m/s) | 3.7 |
| 尺寸 (mm) | 700×310×400（站立）；760×310×200（折叠） |
| 攀爬落差 (mm) | 160 |
| 爬坡角度 (°) | 40 |
| 电池 | 15000 mAh（长续航版） |
| 续航 (h) | 2–4 h |
| 额定电压 (V) | — |
| 电压范围 (V) | 28–33.6 |
| 接口 | Wi-Fi 6、蓝牙 5.2、4G/eSIM |
| 算力 | 8 核高性能 CPU；可选 Orin（40–100 TOPS） |
| 传感器 | 4D 激光雷达 L2、深度相机、足端力传感器、前置摄像头 1280×720 / 120° |

<div class="part-src">
来源：<a href="https://www.unitree.com/cn/go2">https://www.unitree.com/cn/go2</a><br/>
收录：宇树官网 Go2 产品页参数表 + 支持中心核对（2026-10-28）<br/>
核对：2026-10-28
</div>

</div>

<div class="part-comm">
<PartRating part-id="struct-unitree-go2-edu" />
</div>

</div>
  </div>
</div>


## 使用建议

::: warning 按参数推断，不是实测
下面每条都是由这个型号的字段算出来的（公式写在句子里）。
真正的使用经验只能来自用过的人 —— 请写在页尾的讨论里。
:::

- **负载按行走工况算** —— 本行负载取 8 kg（行走口径）。站立静载可能更高，但跑动、越障要按行走负载规划，别拿静载数当动态能力。
- **续航按最差工况留余量** —— 标称 2–4 h。带载、爬坡、低温都会明显缩短，别把空载续航当成交付指标。
- **腿构型决定越障与受力** —— 全膝式、全肘式、前肘后膝（内膝肘）的关节受力与越障姿态不同；同尺寸同质量也不能直接横比爬坡和续航。
- **爬高与爬坡分开看** —— 最大攀爬落差 160 mm、爬坡 40°。落差考验单腿摆高与关节峰值，爬坡考验持续扭矩与抓地。



## 全部参数

| 字段 | 值 |
|---|---|
| 自由度 | 12 |
| 质量 (kg) | 15 |
| 负载 (kg) | 8 |
| 最大速度 (m/s) | 3.7 |
| 尺寸 (mm) | 700×310×400（站立）；760×310×200（折叠） |
| 攀爬落差 (mm) | 160 |
| 爬坡角度 (°) | 40 |
| 电池 | 15000 mAh（长续航版） |
| 续航 (h) | 2–4 h |
| 额定电压 (V) | — |
| 电压范围 (V) | 28–33.6 |
| 接口 | Wi-Fi 6、蓝牙 5.2、4G/eSIM |
| 算力 | 8 核高性能 CPU；可选 Orin（40–100 TOPS） |
| 传感器 | 4D 激光雷达 L2、深度相机、足端力传感器、前置摄像头 1280×720 / 120° |

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

<table class="rs-table"><thead><tr><th>资料</th><th>说明</th></tr></thead><tbody><tr><td><a href="https://www.unitree.com/cn/go2" target="_blank" rel="noopener">官方页面 / 数据出处</a></td><td>本页数字的出处</td></tr><tr><td><a href="https://support.unitree.com/main/zh" target="_blank" rel="noopener">官方文档</a></td><td>接口、引脚与系统说明</td></tr><tr><td><a href="https://github.com/unitreerobotics/unitree_ros/tree/master/robots/go2_description" target="_blank" rel="noopener">URDF / MJCF 模型</a></td><td>官方 / 社区维护的整机模型，可直接导入 PyBullet、MuJoCo、Isaac</td></tr><tr><td><a href="https://github.com/unitreerobotics/unitree_sdk2" target="_blank" rel="noopener">开源项目 1</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td><a href="https://github.com/unitreerobotics/unitree_ros2" target="_blank" rel="noopener">开源项目 2</a></td><td>官方 / 社区维护的 SDK、驱动与例程</td></tr><tr><td class="rs-plain">产品图出处</td><td>宇树官网 Go2 产品页产品图（unitree.com/cn/go2）</td></tr><tr><td class="rs-plain">收录说明</td><td>宇树官网 Go2 产品页参数表 + 支持中心核对（2026-10-28）</td></tr><tr><td><a href="https://www.google.com/search?q=%E5%AE%87%E6%A0%91+Unitree+Go2+EDU+datasheet" target="_blank" rel="noopener">datasheet 检索</a></td><td>厂商常把 PDF 放在产品页附件里</td></tr><tr><td><a href="https://github.com/search?q=Go2+EDU&type=repositories" target="_blank" rel="noopener">SDK / 驱动检索</a></td><td>找现成的 CAN 驱动与示例</td></tr><tr><td><a href="https://www.google.com/search?q=%E5%AE%87%E6%A0%91+Unitree+Go2+EDU+%E4%BB%B7%E6%A0%BC" target="_blank" rel="noopener">价格与货期检索</a></td><td>本站不卖货，报价请向厂商确认</td></tr><tr><td><a href="/semantics" target="_blank" rel="noopener">本站口径说明</a></td><td>这些字段什么意思、缺了代表什么</td></tr></tbody></table>

## 备注

Go2 家族有 AIR / PRO / X / EDU 四个版本，官网 2026-10-28 售价分别为 ¥9,997 / ¥18,600 / ¥29,999 / 联系销售，本条为 EDU。EDU 独有足端力传感器、深度相机与可选 Orin（40–100 TOPS），电池 15000 mAh、续航约 2–4 h；其余版本为 8000 mAh、约 1–2 h。载荷与速度取 EDU 列：载荷 ≈8 kg（极限 ~12 kg），速度 0–3.7 m/s（极限 ~5 m/s）。官网未给 EDU 整机售价，price_cny 留空。

> 每个数字都能在后台查到「谁在什么时候、凭什么改成了现在这样」（`part_edits` 表）。
> 缺的字段一律写 `—`，不猜、不用同类填补、不用额定代替峰值。
