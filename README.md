# Design Minimalist 613

> 一套让设计规则稳定、让项目经验持续增长的极简设计 Skill。

![Design Minimalist 613 overview](docs/images/hero.png)

## 它有什么效果

Design Minimalist 613 把同一套视觉语言应用到不同媒介：固定画板、4px 网格、统一字体 Token、雾感色板与视觉量感规则共同保证输出稳定；项目 preset 再决定当前任务是图片优先、文本优先还是平衡布局。

- **研究型演示**：固定 `1440×810 / 16:9`，一页一个结论，图片或结构图占主体 60–75%。
- **极简简历**：固定 `595×837 / A4`，文本优先，层级、分割线与分页由同一组 Token 约束。
- **网页、PDF 与海报**：浏览可以适配容器，但导出前必须回到 canonical canvas，避免随机断页与版式漂移。

## 每个项目都带一份可复用交付物

Skill 不只保存抽象规范，也保存已脱敏的项目 preset、源实例和资产。Agent 可以先选择最接近的项目，再复用结构与视觉方法，而不是每次从零猜测。

| 项目 | 媒介策略 | 可复用参考 |
|---|---|---|
| `ppt-research` | 16:9、图片优先、一页一结论 | `preset.yaml`、匿名 `example.html`、角色插画资产 |
| `resume-minimal` | A4、文本优先、固定阅读轴 | `preset.yaml`、匿名 `example.html`、canvas contract、抽象头像 |

项目文件位于 `design-minimalist-613/assets/template/projects/`。其中的 `example.html` 是结构参考，不是需要照搬的内容模板。

## 为什么要这样写

![Rules stay stable. Projects keep growing.](docs/images/philosophy.png)

我的设计哲学不是“把风格写成更多规则”，而是把稳定与变化分开：

1. **规则稳定**：网格、字体、色板、视觉量感和固定画板构成通用层。
2. **项目增长**：每次被确认可复用的交付，先沉淀为项目 preset、匿名源实例和特殊资产。
3. **谨慎晋升**：同一做法至少跨两个项目稳定复用后，才建议进入通用层。

这能避免两种常见问题：只有规范、没有真实交付物，导致 Agent 不知道如何落地；或者不断把项目例外写进总规则，最终让规范失去边界。

## Skill 结构

```text
Design_minimalist_613/
├── README.md
├── docs/images/
└── design-minimalist-613/
    ├── SKILL.md
    ├── .skillignore
    ├── references/
    │   ├── GENERAL.md
    │   ├── PROJECTS.md
    │   └── project-registry.json
    ├── scripts/
    │   └── update_project_catalog.py
    └── assets/template/projects/
        ├── ppt-research/
        └── resume-minimal/
```

`SKILL.md` 的 `name` 必须使用小写字母、数字和连字符，并与技能目录名一致。因此仓库展示名可以是 **Design Minimalist 613**，标准技能目录使用 `design-minimalist-613`。

## 使用方式

将 `design-minimalist-613/` 作为完整 Skill 目录安装到支持 Agent Skills 的客户端。触发示例：

- “按 Design Minimalist 613 的规范做一份研究型演示”
- “用现有 resume preset 生成一页 A4 简历”
- “把这次确认的海报方案沉淀进项目库”

新增项目时运行：

```bash
cd design-minimalist-613
python3 scripts/update_project_catalog.py \
  --slug <project-slug> \
  --title "<项目类型>" \
  --canvas "<宽x高 / 比例>" \
  --priority image-first|text-first|balanced \
  --summary "<已泛化的可复用方法>"
```

## 发布格式

本仓库采用开放的 [Agent Skills 目录规范](https://agentskills.io/specification)：每个技能目录至少包含一个带 YAML frontmatter 的 `SKILL.md`，并可按需加入 `scripts/`、`references/` 与 `assets/`。上传到 GitHub 时应保留完整目录结构，而不是只上传 `SKILL.md`。::cite[10]

## 隐私说明

公开版本中的姓名、联系方式、学校、公司、项目名称与业务数据均已删除或替换；示例图像使用匿名插画或抽象占位资产。新增项目进入仓库前，也应先完成同等级别的泛化与脱敏。
