---
name: part-data-research
description: 收集、核对和落库机器人部件资料（关节电机、上位机、下位机、传感器）。当用户要求查找或补充部件型号、价格、参数、图片、官方文档 PDF、官网链接、开源项目链接，或要求新增/修改 data/catalog 条目时使用。执行前必须先完整阅读 docs/data-collection-guide.md。
---

# 机器人部件资料收集

## 强制第一步：先读指南

在做任何搜索、访问官网、修改 JSON 之前，先在工作区根目录完整读取：

`docs/data-collection-guide.md`

当前绝对路径是 `D:\ROBOSelect\RoboSelect\docs\data-collection-guide.md`。每次任务都要重新读一遍，不要凭记忆执行，因为指南可能已经更新。文件不存在时停止，并告诉用户路径缺失，不要跳过。

## 工作流

1. **找型号**：从开源项目、比赛方案、社区 BOM、配置文件、URDF/MJCF、SDK 例程里找真实在用的型号；记录型号、厂商、出现场景和链接。
2. **进官网**：用型号找到厂商官网，翻产品矩阵、选型表、下载中心、文档、GitHub/Gitee；扩展同系列型号，确认版本、电压、接口、内存。
3. **采集**：每个型号收集图片、价格、参数、官方 PDF/文档链接、开源仓库链接。
4. **核对**：核对版本、峰值/额定、转子/输出惯量、控制器存储/功耗/CAN 等口径；关键参数至少两个来源交叉核对；冲突写进 `notes`。
5. **落库**：按 `data/catalog/actuator/<厂商>.json` 的架构写 JSON；上位机放 `controller_high`，下位机放 `controller_low`；图片放 `frontend/public/parts/`。
6. **校验**：运行数据闸门和页面生成，在浏览器验收目录页与型号页。

如果用户只要求调研、不要求落库：完成第 1–4 步，输出候选表和核对结果，不要擅自修改数据文件。

## 硬规则

- 以关节电机模块为架构模板；不要改现有品类的生成页面或生成器来「适配」新数据。
- 缺失字段写 `null`，不省略 key；不要用额定代替峰值，不要猜。
- A 级同 `category/subtype` 的 `specs` 键集必须完全一致。
- `id` 发布后不改；一家厂商一个 JSON 文件。
- 价格必须写来源和日期；活动价注明可能变化。
- `doc_url`、`doc_pdf`、`repo_urls` 必须实际可打开；没有就留空。
- 新增厂商或品类时同步更新 `data/focus.json`。
- 只改数据与图片；`wiki/docs/parts/**` 是生成产物，不手改。

## 校验命令

```bash
./.venv/Scripts/python.exe scripts/check_data.py
./.venv/Scripts/python.exe scripts/build_wiki.py
cd wiki && env -u WIKI_BASE npm run build
```

## 验收清单

- [ ] `check_data.py` 退出码为 0，warning 已逐条看过。
- [ ] `/catalog.html` 的品类计数正确。
- [ ] `/parts/<category>/` 分类表里有新条目。
- [ ] 型号页显示图片、价格、参数、备注、资料链接。
- [ ] 官网、PDF、仓库链接都能打开。
- [ ] `git diff` 没有误改其它品类的生成页面。

## 参考文件

- 收集指南：`docs/data-collection-guide.md`
- 数据目录：`data/catalog/<category>/<vendor>.json`
- 数据闸门：`scripts/check_data.py`
- 页面生成：`scripts/build_wiki.py`