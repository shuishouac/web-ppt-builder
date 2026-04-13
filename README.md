# Web PPT Builder

[English README](./README.en.md)

把一份已经基本定稿的内容大纲，快速做成一个更像 PPT 的网页演示，而不是 `.pptx` 文件。

这个仓库的核心目标是：

- 用 `Slidev` 生成网页式 deck
- 支持两种模式：`内容详实型` 和 `设计优先型`
- 明确品牌、图片、主题和部署输入
- 默认输出可部署到 `Cloudflare Pages` 的静态站点
- 可选导出 `PDF` 方便离线分享

## 适合谁用

适合下面这些场景：

- 你的内容结构已经比较清楚
- 你不想再手工排版 PPT
- 你想要的是“演示风格网页”，不是可编辑的 `.pptx`
- 你希望把这套流程做成一个可以重复使用的本地 AI 工作流

## 核心思路

在开始生成之前，先决定 deck 模式：

- `content-dense` = 内容详实型
  适合让用户不听讲解、只看页面也能理解主要内容。
- `design-led` = 设计优先型
  适合你亲自讲，页面更少字、更强视觉、更依赖图片和节奏。

然后再决定：

- 主题 preset
- 品牌信息
- 图片协作方案
- 部署方式

## 仓库结构

```text
Web PPT Builder/
├── SKILL.md
├── README.md
├── README.en.md
├── deck.config.example.json
├── agents/openai.yaml
├── scripts/
│   ├── scaffold_deck.py
│   └── generate_image_prompts.py
├── references/
│   ├── deck-modes.md
│   ├── intake-template.md
│   ├── image-workflow.md
│   ├── theme-presets.md
│   ├── content-rules.md
│   └── deployment.md
└── assets/starter/
```

## 快速开始

1. 复制 [deck.config.example.json](./deck.config.example.json)，填成你自己的 `deck.config.json`
2. 生成一个 deck 项目：

```bash
python3 scripts/scaffold_deck.py \
  --output "/absolute/path/to/my-deck" \
  --config "/absolute/path/to/deck.config.json"
```

3. 如果图片还没准备齐，生成图片协作包：

```bash
python3 scripts/generate_image_prompts.py \
  --config "/absolute/path/to/deck.config.json"
```

它会生成两份文件：

- `image-prompts.generated.md`
- `image-manifest.generated.json`

这两份文件会直接告诉你：

- 缺哪些图
- 每张图应该叫什么名字
- 应该放到哪个本地路径
- 哪些必须是真图
- 哪些可以用 AI 生成

4. 运行生成出来的 deck：

```bash
cd "/absolute/path/to/my-deck"
pnpm install
pnpm dev
pnpm build
pnpm export:pdf
```

## 图片工作流

这个仓库默认把图片处理成“本地文件夹协作”，而不是聊天里一张张传图。

默认规则：

- 不依赖 chat 上传图片
- 图片统一放到 `public/media/`
- 用系统生成的精确文件名
- 让 AI 后续按文件名匹配，不靠对话记忆

默认判断：

- 真实人物、真实产品、真实证明材料：优先用户提供
- 概念图、章节过渡图、氛围图：可以 AI 生成
- 抠图、扩边、改比例、统一风格：可以 AI 修图

## Cloudflare Pages

默认部署目标是 Cloudflare Pages。

最简单的流程：

1. 本地运行 `pnpm build`
2. 把生成出来的 `dist/` 文件夹上传到 Cloudflare Pages

如果你想接 GitHub 自动部署，也可以把仓库接到 Cloudflare Pages。

## 当前定位

这是一个偏“网页优先”的演示生成 starter。
它不是为了导出可编辑 PowerPoint 而设计的。
