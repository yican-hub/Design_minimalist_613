# PROJECTS｜项目 Presets v0.6

> 主入口之二。使用时只选一个 `project:*`，与 `GENERAL.md` 叠加。所有特殊资产、召回条件、媒介 preset 与项目例外只在本文件维护。

## project:ppt-research

```yaml
project: ppt-research
canvas: {canonical:"1440×810", ratio:"16:9", responsive_reflow:false}
margin: {horizontal:68px, vertical:52px}
priority: image-first
image_area: "60–75%"
wide_image: {threshold:"ratio>=2.0", layout:"top-image/bottom-text"}
type_override:
  display: {size:40px, line:1.15}
  h2: {size:28px, line:1.25}
  body: {size:20px, line:1.45}
  body-emphasis: {size:20px, weight:600, line:1.35}
  label: {size:15px, line:1.35}
  note: {size:13px, line:1.45}
```

- 画板固定为 1440×810；预览只整体缩放，不响应式重排。
- 一页一个结论；图片、数据图或结构图占主体 60–75%，文字只提供结论与阅读路径。
- 宽高比 ≥2.0 的图用上图下文；其他图默认左文右图，图列约为文字列的 1.7–2 倍。
- 图注距图 6–8px，图文 gap 20–24px；图片不加无意义边框、灰底、阴影或渐变。
- 流程节点增多时优先拆页，不无限缩小字号。

### 特殊资产｜六人手绘头像库

- 资源：`assets/template/projects/ppt-research/assets/avatar-library-v3.png`。
- 仅在 Persona、用户旅程、年龄/性别角色或人物视觉需求时召回；无人物需求时不加载。
- 六个字段只按备注召回，**无昵称**：

| 字段 | 备注 / 自动召回条件 |
|---|---|
| `young_m_glasses` | 青年男性；研究/分析场景 |
| `adult_f_longhair` | 成年女性；研究/白领场景 |
| `adult_m_shortcut` | 成年男性；工程/执行场景 |
| `elder_f` | 老年女性；家庭/健康场景 |
| `elder_m` | 老年男性；银发/健康场景 |
| `child_f` | 儿童女性；亲子/教育场景 |

- 整图原始比例 3:2；使用 `width:100%; height:auto; aspect-ratio:3/2; object-fit:contain`，不得裁切或拉伸。

## AutoLoop｜项目例外收敛规则

```yaml
autoloop:
  receive: "发现新的特殊需求或资产"
  first_action: "追加或更新本文件中的对应 project preset"
  promote_to_general: "同一规则至少跨两个项目稳定复用"
  delivery: [GENERAL.md, PROJECTS.md, 变更摘要]
```

- 新特殊需求先追加或更新 `PROJECTS.md` 内对应项目，不直接进入通用规则。
- 至少跨两个项目稳定复用后，才建议将规则迁入 `GENERAL.md`；迁入时保留项目层必要覆盖，不复制同一规则。
- 头像、品牌插画、媒介尺寸、导出约束、项目专属例外均留在本文件。
- 每次修订必须回传最新版 `GENERAL.md`、`PROJECTS.md` 与变更摘要；不再新增第三个维护文档。
## Loop 累积项目

<!-- AUTO_PROJECT:resume-minimal START -->
## project:resume-minimal

```yaml
project: resume-minimal
canvas: "595x837 / A4 print"
priority: text-first
preset: assets/template/projects/resume-minimal/preset.yaml
```

固定单页 595×837 A4；HTML 仅外层等比缩放。L1–L5 同时联动字号、字重、行高与段后距，项目标题统一 L3，正文与技能描述统一 L4；分割线按 section/经历/项目递减。富文本逐项映射源标记，头像使用固定框与稳定资源。默认以 HTML 链接和至少 5×/360DPI 无损 PNG 图片 PDF 保真交付，并用 pdfinfo、pdfimages、html_vision 验证；句末无句号仅在明确要求时同步，事实字段变更后重新生成 PDF。
<!-- AUTO_PROJECT:resume-minimal END -->

<!-- AUTO_PROJECT:personal-web START -->
## project:personal-web

```yaml
project: personal-web
canvas: "1440x920 / fixed hero showcase"
priority: image-first
source: assets/template/projects/personal-web/example.html
preset: assets/template/projects/personal-web/preset.yaml
```

沿用个人网站首屏的左右图文构图、超大标题、人物主视觉与辅助标签；浏览版只整体适配，不改动内部阅读顺序，公开实例替换身份、地点与联系方式。
<!-- AUTO_PROJECT:personal-web END -->
