# GENERAL｜通用设计规范 v0.6

> 主入口之一。先加载本文件，再从 `PROJECTS.md` 选择一个 `project:*` preset。组件只能引用本文件定义的 Token，不在节点内写死样式。

## 01｜网格 × Type

```yaml
space: {u:4px, scale:[4,8,12,16,24,32,48,64,80], section_gap:[24px,32px]}
type:
  family: "PingFang SC, Noto Sans SC, Source Han Sans SC, sans-serif"
  display:       {size:34px, weight:300, tracking:-0.02em, line:1.15, after:24px}
  h2:            {size:22px, weight:500, tracking:0, line:1.30, after:12px}
  body:          {size:16px, weight:400, tracking:0, line:1.60, after:12px}
  body-emphasis: {size:16px, weight:600, tracking:0, line:1.45, after:8px}
  label:         {size:13px, weight:600, tracking:0.04em, line:1.35, after:8px}
  note:          {size:12px, weight:400, tracking:0.02em, line:1.45, after:8px}
```

- 所有空间取自 4px 阶梯；光学修正最多 ±2px，不新增 Token。
- 组件生成必须引用 `type.*`；禁止在组件内局部改字体、字号、字重或行高。
- 项目层只能整体覆盖 Token，不能让单个节点脱离 Type 系统。
- 节点语义与 Type 固定联动：范围 label → `note/label`；卡片标题 → `body-emphasis`；卡片说明 → `note`；结果标题 → `h2`；Loop 标题 → `body-emphasis` 或较小 `h2`；Loop 说明 → `note/body`。切换项目时只覆盖 Token，不改单节点。

## 02｜雾感八色

```yaml
neutral: {bg:#FFFFFF, surface:#F8F6F7, text:#30363D, text2:#59616A, muted:#8A929B, border:#E6E8EA}
palettes:
  red:    {p100:#F7E7E5, p300:#EECFCC, p500:#E6BAB6, p700:#B7837E}
  orange: {p100:#F5E8E0, p300:#EBD2C2, p500:#E2BEA7, p700:#B2886C}
  yellow: {p100:#EFEBDE, p300:#DED8BE, p500:#D1C7A1, p700:#9E9264}
  green:  {p100:#E4EFE4, p300:#CADECA, p500:#B2D0B2, p700:#7A9D7A}
  cyan:   {p100:#DEEFF0, p300:#BEDFE1, p500:#A0D1D4, p700:#609FA2}
  blue:   {p100:#E3ECF7, p300:#C8D9EF, p500:#B0C9E8, p700:#7795BA}
  purple: {p100:#EEE8F5, p300:#DDD2EB, p500:#CEBFE2, p700:#9B88B3}
  gray:   {p100:#E9EBEE, p300:#D5D8DB, p500:#C3C7CC, p700:#8D939A}
```

- 浅底使用深灰字；`p700` 配白字且只用于小标签、关键数字或极少量焦点。
- 强调遵循“最小充分强调”：先使用中浅阶 `p300` + 深灰字；禁止整条宽结果层默认使用 `p700`。
- 切换 palette 时，范围、结果、标签、Loop 与连线的语义色同步切换，不在组件内写死色值。

## 03｜视觉量感对齐

### 3.1 先分类，再对齐

对齐对象先按可见量感分类，而不是先读取 DOM 外框：

| 类别 | 定义 | 首选视觉锚点 |
|---|---|---|
| `mass` | 有填色的面积块 | 相邻 `mass` 或 `surface` 的可见边界 |
| `surface` | 白底或浅底的实体卡片 | 相邻 `surface` 的内容边界、标题基线 |
| `line` | 细边线、虚线语义范围 | 仅表达范围，不主导大色块对齐 |
| `text` | 无容器的纯文字 | 阅读轴、基线与文本块边缘 |

- 同量感对象优先对齐：`mass` 对齐 `mass/surface` 的可见边界；`surface` 对齐相邻 `surface`；不优先把大色块吸附到 `line` 外框。
- 细虚线只表达语义范围，不应成为大面积色块的主视觉锚点。
- 当核心结果层夹在浅底系统中时，优先与上、下白底数据卡片的左右可见边界对齐，而不是与外层虚线组框对齐。
- 几何对齐与视觉对齐冲突时，先保证阅读路径和视觉块连续，再保留语义范围线；允许虚线框比实体内容向四周外扩 16–24px。
- 检查顺序：识别量感 → 找同量感锚点 → 对齐可见边界/基线 → 最后安放范围线与连接线。

### 3.2 视觉重量与最小充分强调

- 大面积重色会产生过强视觉重量。核心结果默认使用 `p300` + `neutral.text`；紫色示例为 `#DDD2EB` + `#30363D`。
- `p700` 只用于小标签、关键数字、序号或极少量焦点；禁止整条宽结果层默认使用 `p700`。
- 判断标准不是“是否用了主题色”，而是强调是否足以建立阅读顺序且没有压过主系统。

## 04｜层级 × 流程

```yaml
flow:
  L1:   {fill:p100, pad:32px}
  L2:   {fill:none, border:"1px dashed p300", pad:"16–24px"}
  L3:   {fill:white, border:"1px solid border", pad:16px}
  key:  {fill:p300, text:text, label:{fill:p700,text:white}}
  Loop: {slot:white, fill:p100, text:text, gap:24px, max_visual_weight:"20%"}
  line: {process:"2px solid p500", feedback:"2px dashed p300", arrow:end}
```

- 固定图示采用 1120×630 canonical canvas；外层保持 16:9，只做整体等比缩放，不重排内部节点。
- 同一分块的列共享 `column tracks`：等宽、同高、同标题基线。上下实体卡片共享左右可见边界；顶层双列和下层三列各自在自己的网格中对齐。
- 外层虚线分组框比实体卡片外扩 16–24px，因此虚线边界不与结果层对齐。
- 结果层跨满实体内容列，与上下白底卡片对齐，不缩成孤岛；默认使用 `p300` 深灰字。
- 主流程实线、反馈虚线；线从边缘锚点出发，不穿文字。
- 有容器边界时，将层级编号、组名与类型合并为单行弱标签，例如 `L2 双列输入 / SURFACE`；只使用 `type.label` 或 `type.note`、普通或中等字重、`neutral.text2` 或项目 `accent-ink`。
- 容器边界已经表达分组，标题只承担说明；不得再拆成多个视觉块，也不得使用深色底标签重复编码层级或分组。

### 4.1 Loop 信息层级生成法

Loop 是辅助机制，不得与主结果争夺视觉焦点。内部信息顺序固定：

1. 英文/类别 label：使用 `type.note` 或 `type.label`。
2. “持续 Loop”标题：使用 `type.body-emphasis` 或较小的 `type.h2`，必须小于主结果标题。
3. 一句机制说明：使用 `type.body` 或 `type.note`，例如“采集失败案例与用户反馈，回流为新样本、标签与约束”。不得与 Loop 标题同字号同字重。
4. 可选动作列表：使用 `type.note`，视觉级别最低。

- Loop 内层使用 `p100` 或 `surface`，外层必须有白色隔离槽；与主内容保留 24px gap；禁止大面积使用 `p500/p700`。
- Loop 的视觉面积与量感建议不超过主内容的 20%；Loop 标题字号不超过结果层标题的 70–80%。
- 先压低面积、色阶与字号，再用结构说明回流关系；不要依靠重色把 Loop 变成第二主角。

## 05｜图文 × 形状

```yaml
layout:
  image_first: {image_area:"60–75%"}
  text_first:  {text_area:"75–90%"}
  wide:   {when:"ratio>=2.0", mode:"top-image/bottom-text"}
  normal: {when:"ratio<2.0", mode:"left-text/right-image", flex:"0.6/1.8"}
  gap:20px
image: {frame:none, background:transparent, fit:contain, caption_gap:8px}
shape: {radius:0, shadow:none, gradient:none, rule:"fill XOR border"}
```

- 先判断信息主角，再分面积；`object-fit:contain` 只防裁切，不能代替合理面积。
- 禁止同时固定图片宽高造成拉伸；图注紧贴图。
- 溢出顺序：图满宽/文字下移 → 精简文字 → 调列宽 → 拆页 → 最后缩图。

## 06｜固定画板渲染合同

- 每个最终产物先选 `canonical canvas`；所有内部尺寸都在 canonical 坐标中设计。
- 禁止响应式重排、节点换行重组或局部缩放。网页预览只整体等比缩放：`scale=min(containerW/canvasW, containerH/canvasH)`。
- 缩放层使用 `transform-origin: top left`；容器保持 canonical `aspect-ratio`；不同屏幕只改变 scale。
- PDF/截图从未缩放的 canonical canvas 直接导出，不从已 `transform:scale(...)` 的 DOM 导出。
- 打印固定 `@page size`、`margin:0`，并开启背景图形（`print-color-adjust:exact`）。
