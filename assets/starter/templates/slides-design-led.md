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

# 核心问题

<v-clicks>

- 用一句话说明这套 deck 要解决什么问题。
- 用一句话说明为什么现在必须看这个问题。
- 用一句话说明听众看完之后要做什么。

</v-clicks>

---
transition: fade
class: mode-__DECK_MODE__
---

<SectionBreak
  eyebrow="Section 01"
  title="问题与判断"
  summary="把背景说明压短，把真正的判断放到前面。"
/>

---
layout: two-cols
transition: slide-up
class: mode-__DECK_MODE__
---

# 现状

- 左边放现状、痛点、误区。
- 每条最多一到两行。
- 如果需要顺序感，使用 `v-click`。

::right::

# 判断

- 右边放你的核心判断。
- 一页只讲一个主要转折。
- 这里适合放对比图或截图。

---
transition: slide-left
class: mode-__DECK_MODE__
---

# 证据 / 案例

| 类型 | 内容 |
| --- | --- |
| 数据 | 一组关键数字 |
| 案例 | 一个最能打的例子 |
| 结论 | 这组证据想证明什么 |

---
transition: slide-right
class: mode-__DECK_MODE__
---

<SectionBreak
  eyebrow="Section 02"
  title="方案或框架"
  summary="把中段做成最容易截图转发的部分。"
/>

---
transition: fade-out
class: mode-__DECK_MODE__
---

# 三步框架

<v-clicks every="1">

1. 第一步：写清楚内容结构
2. 第二步：选对视觉主题
3. 第三步：直接生成网页并发布链接

</v-clicks>

---
transition: slide-left
class: mode-__DECK_MODE__
---

# 下一步

- CTA:
- 联系方式:
- 链接:

> 把最后一页做得像一个明确动作，不要只是“谢谢观看”。
