# CS1332x — Data Structures & Algorithms Journey

> 我学习 GTx CS1332x（Data Structures & Algorithms）的完整记录，作为申请 Georgia Tech OMSCS 项目的准备过程。课程使用 Java，本仓库同时提供 Python 等价实现以巩固两种语言的算法直觉。

## 关于这个仓库

**目标**：在 OMSCS 申请中展示我的：
1. 自驱学习能力（系统性、可追踪的学习记录）
2. 算法与数据结构基础（CS1332 是 OMSCS 强烈推荐的先修课）
3. 工程习惯（commit 规范、文档、测试、双语言实现）

**学习时间线**：开始日期 2026-05-20 — 预计完成 2026-XX-XX

## 仓库结构

```
cs1332-journey/
├── README.md                    ← 你在这里
├── docs/                        ← 学习方法、Git 指南、作品集策略
├── lectures/                    ← 按 module 组织的课程笔记
│   └── module-01-arrays/
│       ├── notes.md
│       ├── ArrayList.java
│       └── tests/
├── assignments/                 ← edX 作业（不含违反学术诚信的内容）
├── notes/
│   ├── weekly/                  ← 每周复盘（用 weekly-template.md）
│   └── concepts/                ← 单个概念的深度笔记
├── python-equivalents/          ← 同算法的 Python 复刻 + pytest 测试
├── practice/
│   └── leetcode/                ← 配套 LeetCode 题解
├── obsidian-vault/              ← 双链概念卡片（Zettelkasten 风格）
│   ├── concepts/                ← 原子概念卡片
│   ├── MOCs/                    ← Maps of Content（主题地图）
│   ├── daily/                   ← 每日笔记
│   └── templates/
└── templates/                   ← 复用模板
```

## 学习节奏

每周一个 module，每个 module 三步走：
1. **Java 学课**（看视频 + 做 edX 作业）
2. **Python 复刻**（同一个数据结构用 Python 重写一遍）
3. **LeetCode 巩固**（3-5 道相关题，写在 `practice/leetcode/`）

每周日做一次复盘（`notes/weekly/`），每月做一次概念地图（Obsidian MOC）。

## 进度追踪

| Module | 主题                  | Java 完成 | Python 复刻 | LeetCode | 复盘  |
| ------ | ------------------- | ------- | --------- | -------- | --- |
| 01     | Arrays & ArrayLists | ⬜       | ⬜         | ⬜        | ⬜   |
| 02     | LinkedLists         | ⬜       | ⬜         | ⬜        | ⬜   |
| 03     | Stacks & Queues     | ⬜       | ⬜         | ⬜        | ⬜   |
| 04     | Trees (BST)         | ⬜       | ⬜         | ⬜        | ⬜   |
| 05     | Heaps & PQs         | ⬜       | ⬜         | ⬜        | ⬜   |
| 06     | HashMaps            | ⬜       | ⬜         | ⬜        | ⬜   |
| 07     | AVL Trees           | ⬜       | ⬜         | ⬜        | ⬜   |
| 08     | Sorting             | ⬜       | ⬜         | ⬜        | ⬜   |
| 09     | Pattern Matching    | ⬜       | ⬜         | ⬜        | ⬜   |
| 10     | Graphs              | ⬜       | ⬜         | ⬜        | ⬜   |
| 11     | Dynamic Programming | ⬜       | ⬜         | ⬜        | ⬜   |

> Module 列表参考 GTx CS1332xI 大纲，开课后以官方为准并修正。

## 学术诚信

本仓库**不包含**任何完整作业答案。`assignments/` 下只放：
- 题目摘要（我自己复述的，不含原题）
- 我的解题思路（高层逻辑）
- 在课程结束 + 至少一学期后再公开的代码

这是 OMSCS 申请的硬要求 — 招生官会查。

## 文档导航

- [高效学习方法指南](docs/study-method.md)
- [Git + GitHub 配置与推送指南](docs/git-github-guide.md)
- [OMSCS 作品集策略](docs/portfolio-strategy.md)

---

*Maintained by Shaonan · Started 2026-05-20*
