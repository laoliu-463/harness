---
name: 提出问题
description: 大事闭环的第一个环节。先判断要不要追问。要追问时，用设计树把问题、真正目标和完成标准问清楚。用户确认简报之后才进入收集信息。开始时按 rules/memory.md 第 2 节搜。
---

# 提出问题

这个技能把多份原技能里对得上「动手之前先问清楚」的做法收成一件事。进入这个技能的都是大事。

## 来源

| 原文 | 用的部分 |
|---|---|
| `sources\pstack\skills\in-your-own-words\SKILL.md` | 用自己的话复述目标和要解决的问题。 |
| `sources\pstack\skills\sharpen\SKILL.md` | 专家会怎么做、用户真正要什么、规格过紧还是过松。该用户决定的选择先留着。 |
| `sources\mattpocock-skills\skills\productivity\grilling\SKILL.md` | 设计树。一轮只问前提已定的问题。每题给推荐答案。事实自己查。理解一致之前不开始做。 |
| `sources\mattpocock-skills\skills\productivity\grill-me\SKILL.md` | 只是 grilling 的入口，不另加步骤。 |
| `sources\mattpocock-skills\skills\engineering\grill-with-docs\SKILL.md` | 追问时把已经定下的术语记下来。 |
| `sources\mattpocock-skills\skills\in-progress\loop-me\SKILL.md` | 追问的产出是规格，不是直接动手。 |
| `sources\mattpocock-skills\skills\engineering\wayfinder\SKILL.md` | 先给终点起名。大到一次会话放不下时，拆成决定，计划做完再动手。 |
| `sources\pstack\skills\figure-it-out\SKILL.md` | Frame。完成要能被证伪。范围写粗数量和花费。撤不回的事更严。长任务开始前先摆出取舍。 |
| `sources\mattpocock-skills\skills\engineering\to-spec\SKILL.md` | 树走完后，把已经谈过的内容收成简报，不再追加追问。 |
| `sources\mattpocock-skills\skills\productivity\to-questionnaire\SKILL.md` | 缺的事实在另一个人那里时，写成问卷交给那个人。 |
| `sources\humanlayer-skills\plugins\design-control-loop\skills\design-control-loop\SKILL.md` | 先找仓库里已有的选项，再谈取舍，同意之后才往下做。 |
| `sources\humanlayer-skills\plugins\rpi\skills\rpi\references\create-prd\process.md` | 第 3 节。先把问题定下来，再定怎样判断做成了。 |
| `rules/memory.md` | 第 2 节。开始时搜。开场简报列出每一条，标明用上、没用上或已过时。 |

## 做什么

开始时按 `rules/memory.md` 第 2 节搜。这一环不往 EverOS 写。读法不在这个技能里重写。

先用自己的话复述用户的目标和要解决的问题。接着问三件已经能问的事：专家会怎么做，用户真正要什么，规格是过紧还是过松。该由用户决定的选择先留着，不替他定。

然后把还没定的决定画成树。一轮只问前提已经定了的问题。每题给出推荐答案，用户回「是」就采纳。事实自己查，不问用户。只有偏好、底线和取舍才问用户。已经定下的术语随手记进简报。

完成标准要写成能被证伪的一句话。范围里写上粗的数量和花费。花钱、对外发消息、重大人生决定单独标成撤不回。大到一次会话放不下时，拆成一个个决定，这一环节不动手实现。

缺的事实如果在另一个人那里，就写成问卷交给那个人，不问用户他答不了的事。选项先从仓库里能找到的做法里提，再谈取舍。

树走完以后，把已经谈过的内容收成开场简报，不再追加追问。用户确认彼此理解一致之前，不进入收集信息。是否进入收集信息，对照这一条判断，并写一句理由。不等用户另外宣布换环节。

开发任务还要到 `harness\sources\` 里找对应技能，读原文后照着做。和 harness 规则冲突时，以 harness 规则为准。仓库和个人规矩见 `modules\03-stage-skills.md` 的开发任务一节。这里不列技能清单。

## 写回任务记录

写进「提出问题」。

- 开场简报：问题、价值标准、投入上限、推荐方案和理由、风险，以及已经定下和还没定的决定。
- EverOS 查到的经验：每一条标明用上、没用上或已过时。没有就写没有。
- 用户原话。

目标、关键取舍、研究范围、投入上限没写明，收集信息不开工。仍需调查的事实可以留下。
