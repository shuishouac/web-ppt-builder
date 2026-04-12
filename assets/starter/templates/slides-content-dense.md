---
theme: default
title: __DECK_TITLE__
titleTemplate: "%s"
info: __DECK_SUBTITLE__
author: __PRESENTER_NAME__
exportFilename: __EXPORT_FILENAME__
drawings:
  persist: false
transition: fade-out
mdc: true
layout: cover
class: mode-__DECK_MODE__
---

<DeckCover
  title="__DECK_TITLE__"
  subtitle="__DECK_SUBTITLE__"
  presenter="__PRESENTER_NAME__"
  role="__PRESENTER_ROLE__"
  organization="__ORGANIZATION_NAME__"
  logo="__LOGO_SRC__"
  headshot="__HEADSHOT_SRC__"
  :show-logo="__SHOW_LOGO__"
  :show-headshot="__SHOW_HEADSHOT__"
/>

---
transition: slide-left
class: mode-__DECK_MODE__
---

# 项目摘要

- 这套 deck 当前选择的是 `__DECK_MODE_LABEL__`
- 目标是让用户即使不听讲解，也能看懂主要结论
- 所以页面会保留更多说明性文字、证据和上下文

> 用这页先建立阅读预期，而不是急着炫设计。

---
transition: fade
class: mode-__DECK_MODE__
---

<SectionBreak
  eyebrow="Section 01"
  title="背景与问题"
  summary="在内容详实型 deck 里，背景和问题需要被解释清楚，而不是只留一句标题。"
/>

---
layout: two-cols
transition: slide-up
class: mode-__DECK_MODE__
---

# 现状与背景

- 这里放完整背景交代。
- 每个点都应该能独立阅读。
- 如果信息很多，拆页，不要缩字。
- 真实图或截图优先用于增强可信度。

::right::

# 关键问题

- 问题一：
- 问题二：
- 问题三：

---
transition: slide-left
class: mode-__DECK_MODE__
---

# 关键判断

- 判断 1：先说结论，再补依据。
- 判断 2：不要怕解释清楚。
- 判断 3：把重要前提写在页内，不要完全依赖口头补充。

---
transition: slide-right
class: mode-__DECK_MODE__
---

# 支撑证据

| 证据类型 | 内容 | 作用 |
| --- | --- | --- |
| 数据 | 一组关键数字 | 证明趋势 |
| 案例 | 一个最强案例 | 建立可信度 |
| 对比 | before / after | 帮助理解差异 |

---
transition: fade
class: mode-__DECK_MODE__
---

<SectionBreak
  eyebrow="Section 02"
  title="方案与执行"
  summary="这一段要让用户直接看到方法、顺序、收益和执行动作。"
/>

---
transition: slide-left
class: mode-__DECK_MODE__
---

# 方案框架

1. 第一步：写清楚内容结构
2. 第二步：补足真实素材和关键截图
3. 第三步：选主题并生成网页 deck
4. 第四步：部署到 Cloudflare Pages

---
transition: slide-left
class: mode-__DECK_MODE__
---

# 下一步与 CTA

- 下一步动作：
- 负责人：
- 时间：
- 联系方式：
- 链接：

> 内容详实型的结尾要更像“行动页”，而不是简单的“谢谢”。
