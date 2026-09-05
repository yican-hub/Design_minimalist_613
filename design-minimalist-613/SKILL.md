---
name: design-minimalist-613
description: 一套可持续积累项目经验的极简设计输出系统，基于固定画板、4px 网格、统一字体 Token、雾感色板和视觉量感规则生成 PPT、简历、网页展示、PDF、海报及结构化流程图；支持复用匿名化项目 HTML 与资产，并在项目确认后通过 Project Loop 将新项目 preset、源实例和特殊规则追加到项目库。适用于“按既有设计规范输出”“复用 design template”“生成跨媒介一致的视觉稿”或“把本次项目沉淀进模板”等场景。
author: Design Minimalist 613
---

# Design Minimalist 613

将设计输出分成“通用规则、项目 preset、实际源实例、项目资产”四层。通用规则保持稳定，项目经验持续增长；新规则先在项目层验证，跨项目稳定后再建议晋升通用层。

## 开始任务

1. 读取 [GENERAL.md](references/GENERAL.md)，建立网格、字体、颜色、视觉量感与固定画板规则。
2. 读取 [PROJECTS.md](references/PROJECTS.md) 和 [project-registry.json](references/project-registry.json)，优先选择最接近的既有项目 preset。
3. 需要复用结构时，从 `assets/template/projects/<project>/` 读取 `preset.yaml`、`example.html` 与 `assets/`；只复用结构和视觉方法，不照搬旧项目内容。
4. 无匹配项目时，从通用层生成新项目；先确定 canonical canvas，再开始排版。

## 固定画板

只要交付物是 PDF、PPT、海报或截图，先锁定画板。浏览型网页可以响应式，但导出前也要切换到固定画板。

默认使用：设计规范与演示型 PDF 为 `1440×810 / 16:9`；PPT 为 `1440×810 / 16:9`；简历与正式文档为 A4；未定义的横版视觉稿先用 `1440×810`，竖版正式文档先用 A4。特殊需求只覆盖画板宽高、比例与页边距，不改写通用 Token。

PDF 按“一模块或一结论一页”组织，从未缩放的 canonical DOM 导出。不要把流式长网页直接交给浏览器随机分页，否则会产生大面积留白和不稳定断页。

## 设计执行

- 所有空间使用 4px 阶梯；组件引用字体 Token，不在单节点写死字号与行高。
- 默认从雾感八色中选择一组语义色阶；同明度与色度切换优先使用既有 palette，不凭自然语言猜测近似色。
- 先区分 `mass / surface / line / text` 的视觉量感，再寻找同量感锚点；虚线只表达范围，不主导大色块对齐。
- PPT 与网页图优先，图片或结构图占主体 60–75%；简历与正式文档文本优先。
- 复杂流程先固定 16:9 画板，再整体缩放预览，不响应式重排内部节点。
- 需要网页实现时，使用 `web-creation` skill 完成页面并部署；需要生成视觉资产时，使用 `image-generate` skill；需要生成 PDF 时遵循固定画板合同。

## Project Loop

每次项目完成后执行以下闭环：

1. **判定是否沉淀**：只有用户确认结果可复用，或明确说“加入项目库 / 记住这个项目”时，才写入项目库。试稿和被否定方案不沉淀。
2. **先泛化再记录**：去除姓名、业务数据和一次性文案，只保留媒介、画板、信息优先级、排版方法、特殊资产类型与可复用例外。
3. **确定项目 slug**：优先更新相同类型；只有画板、媒介优先级或核心结构明显不同，才新增项目。
4. **更新项目库**：运行 [update_project_catalog.py](scripts/update_project_catalog.py)，写入 [PROJECTS.md](references/PROJECTS.md) 与 [project-registry.json](references/project-registry.json)，并按需保存 `example.html`、`preset.yaml` 和项目资产。
5. **检查晋升**：同一规则在至少两个项目中稳定复用时，提出迁入 GENERAL 的建议；未经用户确认，不自动改通用规则。
6. **持久化**：项目库更新后，将当前 `design-minimalist-613` 技能重新上传到目标 Agent 环境，确保后续会话可读取新增项目。

新增或更新项目：

```bash
python3 scripts/update_project_catalog.py \
  --slug <project-slug> \
  --title "<项目类型>" \
  --canvas "<宽x高 / 比例>" \
  --priority image-first|text-first|balanced \
  --summary "<已泛化的可复用方法>" \
  [--preset-file <preset.yaml>] \
  [--example-html <example.html>] \
  [--asset-dir <assets目录>]
```

## 输出检查

交付前确认：画板尺寸明确；内部未响应式重排；字体、间距与颜色来自 Token；图片未拉伸；流程图线条不穿文字；PDF 每页完整且没有异常大面积留白；项目专属内容没有错误晋升为通用规则；项目实例不含个人身份、联系方式或真实业务数据。
