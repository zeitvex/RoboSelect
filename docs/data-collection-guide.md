# 部件资料收集指南

> 适用范围：关节电机、上位机（`controller_high`）、下位机（`controller_low`），以及后续的传感器品类。
>
> 目标：把「在开源项目里看到的一个东西」变成一条可校验的数据：**有型号、有官网出处、有图、有价格、有参数、有官方文档、有开源项目链接**。
>
> 总原则：**先找真实在用的型号，再顺着型号进官网；先拿到出处，再填数字；查不到就写 `null`，不猜。**

---

## 0. 全流程

```text
开源项目 / 比赛方案 / 社区 BOM
        │
        │  找到型号字符串（如 DM-J4310-2EC、RDK X5、RoboMaster C 板）
        ▼
厂商官网：产品矩阵 / 选型表 / 下载中心 / 文档 / GitHub·Gitee
        │
        │  扩展同系列型号，确认版本、电压、接口、内存
        ▼
逐项采集：图片 / 价格 / 参数 / 官方 PDF / 文档链接 / 开源仓库
        │
        ▼
按关节电机模块的 JSON 架构落库
        │
        ▼
check_data.py → build_wiki.py → 浏览器验收
```

---

## 1. 第一步：从开源项目和真实使用找型号

不要一上来就翻厂商目录。先回答一个问题：**做这类机器人的人，实际在用什么？**

### 1.1 搜索入口

| 入口 | 怎么搜 | 能发现什么 |
|---|---|---|
| GitHub 项目 | `quadruped robot BOM`、`legged robot`、`open source robot dog`、`robot arm BOM` | 整机方案、硬件清单、在用型号 |
| GitHub 代码 | 直接搜型号：`DM4310`、`DM-J4310`、`RoboMaster`、`RDK X5`、`Jetson Orin` | 配置文件、URDF/MJCF、驱动、例程 |
| GitHub 组织 | 厂商官方组织下的 SDK / examples / hardware 仓库 | 官方支持的型号列表、通信协议 |
| 比赛方案 | RoboMaster、电赛、机器人竞赛的技术报告 / BOM | 大批量使用、经过实战验证的型号 |
| 论文与测评 | 硬件章节、实验平台表、开源复现项目 | 型号 + 使用场景 + 对比对象 |
| 社区 | 知乎、B站、CSDN、Reddit、Discord、QQ 群 | 线索和踩坑记录，不作为参数最终来源 |
| 电商 | 淘宝、京东搜型号 | 确认在售型号、版本、参考价；参数仍回官网核对 |

### 1.2 从项目反查部件

拿到一个开源项目后，按这个顺序找：

1. **BOM / 硬件清单**：`BOM.md`、`hardware/`、`docs/`、`README` 的物料表。
2. **配置文件**：`config.yaml`、`robot.yaml`、URDF、MJCF、`params.json` 里的执行器型号。
3. **代码依赖**：SDK、CAN 驱动、示例程序里出现的电机/主控型号。
4. **Issue / Discussion**：搜索「replacement」「alternative」「burned」「upgrade」，常能看到真实替代型号。
5. **图片与视频**：确认实物形态，避免把整机型号当成部件型号。

记录候选时至少写清楚：

| 型号 | 厂商 | 在哪个项目/场景出现 | 链接 | 待确认 |
|---|---|---|---|---|
| DM-J4310-2EC V1.2 | 达妙 DAMIAO | 某开源四足关节 | 项目 BOM 链接 | 电压、价格、版本 |
| RDK X5 8GB | 地瓜机器人 | 某视觉导航方案 | 项目 README | 4GB/8GB、是否含配件 |
| RoboMaster C 板 | 大疆 DJI | 某平衡车/云台方案 | 项目硬件清单 | 是否含电调 |

### 1.3 例：DM4310 是怎么找到的

1. 在开源四足项目的 BOM 或配置里看到 `DM-J4310-2EC`。
2. 搜索 `DM-J4310-2EC`，找到达妙官网/官方仓库。
3. 进入官网的产品中心或选型表，发现这不是孤零零一个型号，而是一整个系列：
   `DM-J4310`、`DM-J4340`、`DM-J6006`、`DM-J8009`、`DM-J10010`、`DM-JH` 系列等。
4. 按「电压、减速比、通信接口、峰值/额定扭矩、价格」逐项对比，决定哪些型号值得收录。
5. 不是只收最初看到的那一个，而是把官网同系列里**常用且有公开资料**的型号补全。

### 1.4 控制器同理

- 开源项目里看到 `RDK X5` → 进 D-Robotics 官网 → 看到 X3 / X5、4GB / 8GB 等版本。
- 看到 `Jetson Orin Nano` → 进 NVIDIA 官网 → 看到 Orin Nano / NX / AGX、模组 / 开发套件。
- 看到 `RoboMaster C 板` → 进 RoboMaster 官网 → 看到 A 板 / C 板及配套电调。

控制器尤其要区分：**核心板、模组、开发套件、含电源/外壳的整机套件**不是同一条数据。

---

## 2. 第二步：进官网，从一个型号扩展到一个系列

### 2.1 先确认「官网」

搜索 `<厂商名> <型号> official` 或 `<厂商名> 官网`，确认：

- 域名是不是厂商主站，而不是经销商、淘宝店、资料搬运站。
- 中文站和国际站是否同一代产品，参数是否一致。
- 旧域名、旧产品页是否还在，是否已经被新产品替代。
- 关节电机厂商尤其常见「总站 + 商城 + 文档站 + Gitee/GitHub」多入口并存，以当前官网产品页和选型表为准。

### 2.2 官网上必须翻的 5 个位置

| 位置 | 要找什么 | 落库字段 |
|---|---|---|
| 产品中心 / 产品矩阵 | 同系列还有哪些型号、哪些已停产 | `model`、`title`、`url` |
| 选型表 / 规格书 | 峰值/额定、减速比、电压、电流、尺寸、重量 | `specs` 数值 |
| 下载中心 | 数据手册、用户手册、2D/3D 图、固件 | `doc_pdf` |
| 文档 / Wiki / 开发者中心 | 接口定义、引脚、系统镜像、SDK 用法 | `doc_url` |
| GitHub / Gitee 组织 | 官方 SDK、驱动、例程、模型仓库 | `repo_urls` |

### 2.3 扩展型号的规则

- **同系列不同减速比、电压、通信、编码器**：分别建条，不合并。
- **同型号不同内存/存储**：参数或价格有差异就分条，例如 4GB / 8GB。
- **模组 vs 开发套件**：分开建条；套件要在 `notes` 写清包含什么。
- **新旧版本**：如 V1.1 / V1.2，分别建条；旧版本保留并注明，不静默删除。
- **只有整机没有部件页**：不要把整机参数硬填进部件字段；找不到就留空。
- **官网没有的型号**：回到开源项目、经销商或厂商客服确认，不靠猜。

### 2.4 例：官网扩展

- 达妙 DM4310 → 官网产品矩阵 → J4310 / J4340 / J6006 / J8009 / J10010 / JH 系列。
- 地瓜 RDK X5 → 官网 → X3 / X5、4GB / 8GB。
- NVIDIA Jetson Orin Nano → 官网 → Orin Nano / NX / AGX、模组 / 开发套件。
- 大疆 RoboMaster C 板 → 官网 → A 板 / C 板、配套电调与底盘。

---

## 3. 第三步：每个型号要采的资料

### 3.1 基础信息（顶层字段）

| 字段 | 要求 | 示例 |
|---|---|---|
| `id` | 全库唯一，发布后不改 | `达妙-dm-dm-j4310-2ec-v1-2` |
| `category` | 品类 | `actuator` / `controller_high` / `controller_low` |
| `subtype` | 子类，沿用同品类现有值 | `planetary` / `sbc` / `mcu` |
| `vendor` | 中文名 + 英文缩写 | `达妙 DAMIAO` |
| `vendor_cn` | 纯中文名 | `达妙科技` |
| `model` | 官方型号，保留版本号 | `DM-J4310-2EC V1.2` |
| `title` | 页面标题，厂商 + 型号 | `达妙 DM-J4310-2EC V1.2` |
| `url` | 本页数字的官方出处 | 官方产品页 / 选型表 |
| `source_tier` | `A` / `B` / `C` | 见 4.4 |
| `verified` | 必须显式写 `0` 或 `1` | `1` |
| `last_checked` | 核对日期，ISO 格式 | `2026-10-28` |
| `price_cny` | 人民币参考价；无公开价写 `null` | `599` |
| `origin` | 数据来源与日期 | `达妙 2026 产品选型表 2026-10-23` |
| `notes` | 口径、版本、价格条件、坑 | 见 3.3 |
| `search` | 小写搜索词，含中英文和型号变体 | `达妙 dm dm-j4310-2ec v1.2` |

### 3.2 图片

- 优先使用**官网产品页的官方产品图**，不要用整机图、展会图、带店铺水印的图。
- 官网是 SPA、页面里没有 `<img>` 时，可以从 `og:image`、产品 JSON、官方 CDN 找图。
- 下载后必须实际打开看一眼：型号对不对、是不是黑图、有没有裁掉接口/铭牌。
- 图片放到 `frontend/public/parts/`，文件名用 `<厂商>-<型号>.<jpg|png|webp>`。
- `image_url` 写 `/parts/<文件名>`；`image_source` 写清图片来自哪个页面/哪个栏目。
- 官方图实在找不到时，宁可不放图（`image_url: null`），不要拿相似型号顶替。

### 3.3 价格

- `price_cny` 只放**公开可查的参考价**，币种统一人民币。
- 在 `notes` 里写清：**哪个页面、哪天、什么条件**。
- 必须区分：
  - 裸板 / 开发套件 / 含电源外壳的整机；
  - 4GB / 8GB、V1.1 / V1.2；
  - 官方指导价 / 渠道价 / 活动价 / 教育优惠；
  - 单件价 / 批量价 / 含税含运费价。
- 活动价不会长期有效，写「活动价，可能随活动结束变化」，不要伪装成稳定报价。
- 没有公开价格就写 `null`，不要用「大概」「听说」填数。

### 3.4 参数

#### 关节电机（`actuator`）

| 字段 | 含义 / 采集提示 |
|---|---|
| `tau_peak_Nm` | 峰值扭矩，必须能说明测试条件 |
| `tau_rated_Nm` | 额定扭矩；厂商只给额定就只填额定 |
| `tau_basis` | `peak` / `rated`，有峰值时必须填 |
| `speed_noload_rpm` | 空载转速 |
| `speed_rated_rpm` | 额定转速 |
| `gear` | 减速比；直驱写 `1` |
| `mass_kg` | 整机质量，含减速器/编码器/外壳 |
| `od_mm`、`l_mm` | 外径、长度；写清是否含轴/接插件 |
| `rotor_inertia_kgm2` | 电机侧转子惯量 |
| `inertia_basis` | `rotor` / `output`；与转子惯量同时给或同时为空 |
| `armature_kgm2` | 折算到输出端的等效惯量，必须满足 `armature = N² × rotor_inertia` |
| `voltage_V`、`voltage_range_V` | 额定电压、允许范围 |
| `kt_Nm_per_A` | 扭矩常数 |
| `r_phase_ohm`、`l_phase_uh` | 相电阻、相电感 |
| `pole_pairs` | 极对数 |
| `i_peak_A`、`i_rated_A` | 峰值/额定电流 |
| `encoder` | 编码器类型（磁编/光编、单编/双编、绝对值/增量） |
| `comm` | 通信接口（CAN、CANFD、EtherCAT 等） |
| `driver_integrated` | 是否内置驱动 |
| `ip` | 防护等级；没公布写 `null` |
| `image_url`、`image_source` | 产品图路径与出处 |

#### 上位机（`controller_high`）

`soc`、`cpu`、`cores`、`cpu_arch`、`gpu`、`cuda_cores`、`npu_tops`、`ram_gb`、`ram_bw_gbs`、`storage_gb`、`power_idle_w`、`power_max_w`、`os`、`cuda`、`ros2`、`eth`、`usb`、`can`、`csi`、`pcie`、`size_mm`、`weight_g`。

采集时注意：

- NPU 的 TOPS 要写清是 INT8 稠密还是稀疏，不要跨平台直接按 TOPS 比。
- `storage_gb` 指板载存储；只支持 microSD / 需要自购 NVMe 的写 `null`，并在 `notes` 说明。
- `power_idle_w` / `power_max_w` 是整板功耗，不是模组 TDP。
- `can` 写控制器路数；无原生 CAN 写 `0` 或 `null`，并说明是否需要外扩。
- `usb`、`eth`、`csi`、`pcie` 写清数量和版本。

#### 下位机（`controller_low`）

`mcu`、`clock_mhz`、`ram_kb`、`flash_kb`、`foc_axes`、`canfd`、`can`、`current_loop_khz`、`torque_mode`、`voltage_in_V`、`voltage_max_V`、`comm_upper`。

采集时注意：

- **主控板不等于电机驱动器**：没有集成 FOC 功率级时 `foc_axes` 留 `null`，在 `notes` 明确写「需外接电调/驱动器」。
- `can` 写物理路数，`canfd` 单独写布尔值；不要把「支持 CAN FD」当成路数。
- `current_loop_khz` 只有厂商明确公布才填。
- `voltage_in_V` / `voltage_max_V` 写输入范围；电池供电的要注明几 S。

#### 通用

`size_mm` 写 `长×宽×高` 或 `长×宽`，单位 mm；`weight_g` 单位 g。尺寸要注明是否含散热片、接插件、外壳。

### 3.5 官方文档与开源项目

这三个字段放在 `specs` 里，但**不进入参数表**，只出现在页面「资料与链接」：

| 字段 | 要求 |
|---|---|
| `doc_url` | 官方文档 / Wiki / 开发者中心链接；接口、引脚、系统说明 |
| `doc_pdf` | 官方 PDF 的**直链**（datasheet / 用户手册 / 选型表）；不是下载页 |
| `repo_urls` | 官方 SDK、驱动、例程仓库；社区项目可以放，但要确认与型号相关 |

规则：

- 官方优先。官方仓库里的 raw PDF 也算官方 PDF，但要确认版本与型号匹配。
- 链接必须实际打开验证，不能是 404、登录墙或网盘。
- 没有就写 `null` / `[]`，不要用搜索结果页凑数；页面会自动生成检索入口。
- 同一链接不用重复放；生成器会去重。

---

## 4. 第四步：核对口径，别把不同东西填进同一个字段

### 4.1 先确认「是不是同一个东西」

- 型号版本：V1.1 / V1.2 / V2.0 可能参数不同。
- 电压版本：24V / 48V 可能是两个型号。
- 通信版本：CAN / CANFD / EtherCAT 可能价格不同。
- 控制器版本：4GB / 8GB、模组 / 套件、带电源 / 不带电源。
- 配件边界：电机是否含线缆、驱动器是否含散热片、开发板是否含电源。

### 4.2 容易混的口径

| 容易混的 | 正确做法 |
|---|---|
| 峰值扭矩 vs 额定扭矩 | 分子写清；峰值必须能说明持续时间与初始温度 |
| 转子惯量 vs 输出端惯量 | `inertia_basis` 如实写；`armature` 必须等于 `N² × J` |
| NPU TOPS | 写清 INT8 稠密/稀疏；不要跨平台直接比值 |
| 板载存储 vs 可扩展存储 | `storage_gb` 只写板载；microSD/NVMe 写在 `notes` |
| 整板功耗 vs 模组 TDP | `power_*_w` 写整板实测/标称，并注明条件 |
| CAN 路数 vs CAN FD | `can` 是路数，`canfd` 是布尔值 |
| 裸板价 vs 套件价 | `price_cny` 写对应版本，`notes` 写包含什么 |
| 官方指导价 vs 活动价 | 写日期和条件，不把活动价当长期价 |

### 4.3 交叉核对

- 关键参数至少核对**两个来源**：官网产品页 + 规格书/用户手册；有冲突时以更新的官方规格书为准。
- 冲突不要静默覆盖，写进 `notes`，保留两个口径。
- 物理量明显不合理时先查单位：mm/cm、g/kg、mNm/Nm、μ/µ。
- 价格与参数分开核对：电商页面可以确认价格，但参数回官网。

### 4.4 来源等级

| 等级 | 定义 | 典型来源 |
|---|---|---|
| `A` | 官方 datasheet / 选型表逐项核对 | 官方 PDF、官方规格页、官方手册 |
| `B` | 厂商页面或广泛引用，未逐项复核 | 产品介绍页、经销商页面、社区整理 |
| `C` | 二手来源 | 论坛、视频、个人博客、道听途说 |

同时必须显式写 `verified`（0/1）和 `last_checked`。A 级行在同一个 `category/subtype` 下必须**键集完全一致**：缺的字段写 `null`，不能少 key。

---

## 5. 第五步：落库，照关节电机模块的架构

### 5.1 文件结构

```text
data/catalog/
  actuator/<厂商>.json          ← 关节电机，一家一个文件
  controller_high/<厂商>.json   ← 上位机
  controller_low/<厂商>.json    ← 下位机
frontend/public/parts/          ← 产品图
```

- 一家厂商一个 JSON 文件，文件里是数组，一个型号一条记录。
- **不要**按型号拆文件；小 PR 只改自己厂商的文件。
- 新增厂商或品类时，同步更新 `data/focus.json` 的 `categories` / `vendors`，否则采集脚本重跑时会被当成范围外数据过滤掉。
- `wiki/docs/parts/**` 是生成产物，**不要手改**。

### 5.2 顶层字段

所有品类共用同一套外壳：

```json
{
  "id": "...",
  "category": "actuator",
  "subtype": "planetary",
  "vendor": "...",
  "vendor_cn": "...",
  "model": "...",
  "title": "...",
  "url": "...",
  "source_tier": "A",
  "verified": 1,
  "last_checked": "2026-10-28",
  "price_cny": 599,
  "specs": {},
  "notes": "...",
  "origin": "...",
  "search": "..."
}
```

### 5.3 关节电机完整示例

```json
{
  "id": "达妙-dm-dm-j4310-2ec-v1-2",
  "category": "actuator",
  "subtype": "planetary",
  "vendor": "达妙 DAMIAO",
  "vendor_cn": "达妙科技",
  "model": "DM-J4310-2EC V1.2",
  "title": "达妙 DM-J4310-2EC V1.2",
  "url": "https://www.hightorque.cn/",
  "source_tier": "A",
  "verified": 1,
  "last_checked": "2026-10-28",
  "price_cny": 599,
  "specs": {
    "tau_peak_Nm": 12.5,
    "tau_rated_Nm": 3.5,
    "tau_basis": "peak",
    "speed_noload_rpm": 450,
    "speed_rated_rpm": 120,
    "gear": 10,
    "mass_kg": 0.306,
    "od_mm": 57,
    "l_mm": 46,
    "rotor_inertia_kgm2": 0.00002,
    "inertia_basis": "rotor",
    "armature_kgm2": 0.002,
    "voltage_V": 48,
    "voltage_range_V": "15~52",
    "kt_Nm_per_A": 0.924,
    "r_phase_ohm": 0.58,
    "l_phase_uh": 320,
    "pole_pairs": 14,
    "i_peak_A": 20,
    "i_rated_A": 4.8,
    "frictionloss_Nm": null,
    "damping_Nms_rad": null,
    "encoder": "磁编，双编",
    "comm": "CAN、CANFD",
    "driver_integrated": true,
    "ip": null,
    "image_url": "/parts/dm-dm-j4310-2ec-v1-2.jpeg",
    "image_source": "达妙官网产品图"
  },
  "notes": "48V 版本；额定 3.5 N·m；价格来源：达妙天猫旗舰店商品页（2026-10-28 抓取，活动价可能变化）。",
  "origin": "达妙 2026 产品选型表 2026-10-23",
  "search": "达妙 dm dm-j4310-2ec v1.2 达妙科技 can canfd"
}
```

### 5.4 控制器套用同一架构

上位机示例（字段值略，结构不变）：

```json
{
  "id": "cont-drobotics-rdk-x5-8gb",
  "category": "controller_high",
  "subtype": "sbc",
  "vendor": "地瓜机器人 D-Robotics",
  "vendor_cn": "地瓜机器人",
  "model": "RDK X5 8GB",
  "title": "地瓜机器人 RDK X5 8GB",
  "url": "https://developer.d-robotics.cc/rdkx5",
  "source_tier": "A",
  "verified": 1,
  "last_checked": "2026-10-28",
  "price_cny": 699,
  "specs": {
    "soc": "Sunrise 5",
    "cpu": "8× Cortex-A55 @1.5GHz",
    "cores": 8,
    "cpu_arch": "arm64",
    "gpu": "32 GFLOPS",
    "cuda_cores": null,
    "npu_tops": 10,
    "ram_gb": 8,
    "ram_bw_gbs": null,
    "storage_gb": null,
    "power_idle_w": null,
    "power_max_w": null,
    "os": "Ubuntu 22.04 (RDK OS)",
    "cuda": false,
    "ros2": true,
    "eth": "1× GbE (PoE)",
    "usb": "4× USB 3.0 Type-A + 1× USB 2.0 Type-C",
    "can": 1,
    "csi": 2,
    "pcie": null,
    "size_mm": "85×56",
    "weight_g": null,
    "image_url": "/parts/rdk-x5-8gb.jpg",
    "image_source": "D-Robotics 官网 RDK X5 产品页产品图",
    "doc_url": "https://developer.d-robotics.cc/rdkx5",
    "doc_pdf": null,
    "repo_urls": [
      "https://github.com/D-Robotics/rdk_model_zoo",
      "https://github.com/D-Robotics/hobot_dnn"
    ]
  },
  "notes": "8GB 版；板载无 eMMC，系统跑 microSD；价格与版本条件写清。",
  "origin": "D-Robotics 官网产品页 + 规格表核对（2026-10-28）",
  "search": "d-robotics rdk x5 8gb sunrise 5"
}
```

下位机只需替换 `category` / `subtype` / `specs` 字段为 `mcu`、`clock_mhz`、`ram_kb`、`flash_kb`、`foc_axes`、`canfd`、`can`、`current_loop_khz`、`torque_mode`、`voltage_in_V`、`voltage_max_V`、`comm_upper` 等，外壳完全一致。

### 5.5 页面结构对应关系

关节电机模块的页面结构由数据字段直接驱动，新增品类也沿用同一套：

| 页面区块 | 数据来源 |
|---|---|
| 官方参数 | `specs` 中的核心字段 |
| 使用建议 / 指标 | 由 `specs` 计算，只对关节电机生成深度指标 |
| 全部参数 | 除图片和资料链接外的全部 `specs` |
| 优惠与获取条件 | `price_cny` + `data/offers/*.json` |
| 资料与链接 | `url`、`doc_url`、`doc_pdf`、`repo_urls`、`image_source`、`origin` |
| 备注 | `notes` |
| 实际使用 / 评分 | GitHub issue 聚合，不在 JSON 里手写 |

### 5.6 命名约定

- `id` 全库唯一，发布后不改；同品类沿用已有风格：
  - 关节电机：`达妙-dm-dm-j4310-2ec-v1-2`
  - 控制器：`cont-drobotics-rdk-x5-8gb`
- 文件名 = 厂商 slug，如 `damiao.json`、`dji.json`、`drobotics.json`。
- `search` 用小写，包含厂商、型号、中文名、接口等搜索词。
- 图片文件名与型号对应，不覆盖别的型号的图。

---

## 6. 第六步：校验与发布

```bash
# 1. 数据闸门
./.venv/Scripts/python.exe scripts/check_data.py

# 2. 生成文档站内容
./.venv/Scripts/python.exe scripts/build_wiki.py

# 3. 构建静态站
cd wiki
env -u WIKI_BASE npm run build

# 4. 重启后端，让 seed_catalog 重新灌库
cd ../backend
../.venv/Scripts/python.exe -m uvicorn app.main:app --reload --port 8000
```

### 验收清单

- [ ] `check_data.py` 退出码为 0；warning 已逐条看过。
- [ ] A 级同 `category/subtype` 的行键集完全一致。
- [ ] `/catalog.html` 的品类计数正确。
- [ ] `/parts/<category>/` 分类表里有新条目。
- [ ] 型号页能显示图片、价格、参数、备注。
- [ ] 「资料与链接」里的官网、PDF、仓库都能打开。
- [ ] 图片路径正确，不是黑图、错图、整机图。
- [ ] `git diff` 里没有意外改到其它品类的生成页面。

---

## 7. 常见坑

1. **把整机型号当部件型号**：搜到的是机器人，不是关节电机/主控板。
2. **官网是 SPA，抓不到图**：优先找 `og:image`、产品 JSON、官方 CDN；下载后必须目检。
3. **PDF 给的是下载页而不是直链**：点开确认能直接看到 PDF。
4. **GitHub 仓库 404**：官方组织名、仓库名可能已迁移；用官网链接或 Gitee 镜像核对。
5. **把不同版本合并成一条**：V1.1 / V1.2、4GB / 8GB、裸板 / 套件必须分开。
6. **活动价当长期价**：`notes` 写日期和条件，价格随时可能变。
7. **用额定扭矩冒充峰值**：`tau_basis` 必须如实；没有峰值就留 `null`。
8. **armature 不等于 N²×J**：数据闸门会直接报错。
9. **主控板写成电机驱动器**：没有 FOC 功率级的 `foc_axes` 必须为 `null`，并在备注说明。
10. **为了让页面好看去改生成器**：新增品类/字段才动生成器；改完必须确认旧品类页面 `git diff` 为空。

---

## 8. 最小提交清单

一次 PR 只做一件事：

- [ ] 新增/修改 `data/catalog/<category>/<厂商>.json`
- [ ] 新增产品图到 `frontend/public/parts/`
- [ ] 补齐 `image_url`、`image_source`、`doc_url` / `doc_pdf` / `repo_urls`
- [ ] 在 `notes` 写清价格来源、日期、版本与口径
- [ ] 跑过 `check_data.py`
- [ ] 跑过 `build_wiki.py`，并检查生成页面
- [ ] 没有手改 `wiki/docs/parts/**` 等生成产物