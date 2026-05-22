# OMSCS 申请角度的 GitHub 作品集策略

> 这份策略文档讨论：(1) OMSCS 招生官在 GitHub 上看什么、(2) 你的 GitHub 该长什么样、(3) `cs1332-journey` 之外你接下来一年要建哪些 repo。

## 0 · 一个直觉校准

**OMSCS 不是 PhD 项目。** 招生官不会找你"做出过 SOTA 模型"或"发过 NeurIPS"。这是一个**专业硕士项目**，他们想看的是：

1. **你能不能学得动 CS 课**（CS1332 + 一两门技术课的证书已经基本覆盖）
2. **你能不能完成长期项目**（GitHub commit graph 是直接证据）
3. **你能不能写清楚自己在干什么**（README、commit message、博客）
4. **你有没有诚信**（没有抄答案、没有买的 repo）

录取率约 60–75%，门槛不是天才，是**完整性**。一个**真**的 GitHub > 一个**漂亮但假**的 GitHub。

---

## 1 · 招生官在 30 秒里能看到什么

想象一下他/她在浏览器里打开 `github.com/shaonan-yz` (假设)，看到：

```
[头像] Shaonan
       Finance & ops background, now building ML/data + CS foundations 
       for OMSCS application.
       📍 ...   🔗 ...
       
       Pinned repositories
       ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
       │ cs1332-journey   │  │ python-finance-  │  │ omscs-prep-      │
       │ ★ 2 📌           │  │ utils ★ 5        │  │ math-refresh ★ 1 │
       │ Java + Python    │  │ My toolkit from  │  │ Linear algebra & │
       │ implementations  │  │ years of finance │  │ stats refresher  │
       │ of CS1332 DSA    │  │ work...          │  │ in Jupyter       │
       └──────────────────┘  └──────────────────┘  └──────────────────┘
       
       [深绿色贡献日历，连续 60 天有 commit]
```

**30 秒里他/她能得出的判断**：
- ✅ 在认真学 DSA（CS1332 是 OMSCS 信号弹）
- ✅ 有真实工作背景做差异化（金融）
- ✅ 主动补数学基础（OMSCS ML 方向必须）
- ✅ 持续性强（贡献日历）
- ✅ 能写英文 README（沟通能力）

这就是目标。

---

## 2 · 你的"理想"GitHub 个人主页

### Pinned repos（最多 6 个，挑 3–6 个最能讲故事的）

我建议你一年内建到这个组合：

| 类别        | Repo 例子                                                 | 想传达的信号                   |
| --------- | ------------------------------------------------------- | ------------------------ |
| **学术准备**  | `cs1332-journey`                                        | "我在系统准备 OMSCS 先修"        |
| **学术准备**  | `omscs-math-refresh`（线性代数、概率论的 Jupyter 复习笔记）            | "我知道 OMSCS ML/AI 方向需要这些" |
| **背景差异化** | `finance-toolkit`（用 Python 把你过去金融/运营工作里反复做的事自动化）        | "我有 5 年真实业务背景" — 招生官稀缺这种 |
| **应用 ML** | `<一个小项目，例如>portfolio-optimizer` 或 `<某个业务场景>-classifier` | "我把 ML 用到了我懂的领域"         |
| **工程能力**  | 一个有 tests + CI + 体面 README 的 Python 包，发到 PyPI 也行        | "我能交付可维护的代码"             |
| **学习能力**  | `learning-log` 或博客 repo（用 GitHub Pages 跑）               | "我会写、会反思"                |

**不要做的事**：
- 不要 fork 别人的项目然后给自己挂名（一眼就看穿）
- 不要建 50 个空 repo（数量不是质量）
- 不要 push 教程的复制粘贴代码（"我跟着 Coursera 做的 todo app"）

### GitHub Profile README

去 https://github.com/<你的 username>/<你的 username>（同名 repo）创建 README — 它会显示在你主页顶部。

模板：

```markdown
# Hi, I'm Shaonan 👋

I spent the last several years in finance, operations, and data analytics, 
and I'm now systematically building the CS foundations to apply to 
**Georgia Tech's OMSCS** (Computing Systems / ML specialization).

### What I'm working on right now

- 📚 **CS1332x** (Data Structures & Algorithms) → [cs1332-journey](link)
- 🧮 **Math refresh** for ML coursework → [omscs-math-refresh](link)
- 💼 **Finance × Python**: turning my domain knowledge into tools → [finance-toolkit](link)

### Tech I work with

Python (primary) · pandas · scikit-learn · Java (learning for DSA) · SQL · Git

### About me

- 🎯 Goal: OMSCS Fall 2027
- 📝 I write about what I learn at [your blog or learning-log]
- 📫 Reach me at yzwsn2024@gmail.com
```

**关键**：第一句话就讲清楚你是谁、要去哪里。招生官 7 秒决定要不要继续读。

---

## 3 · `cs1332-journey` 这个 repo 怎么"为招生官写"

招生官点进来 30 秒能看到什么？三个东西：

### (a) README 顶部一段 elevator pitch
我们已经写了 — "我学习 GTx CS1332x 的完整记录，作为申请 GT OMSCS 的准备过程"。**第一句必须告诉读者：你在干什么，为什么。**

### (b) Progress tracker 表格
那个 ✅/⬜ 的表 — 招生官一眼能看出你完成度。如果到申请那天表格全是 ✅，配合 commit graph 是黄金组合。

### (c) Commit graph 的形状
一周 push 3–5 次比一天 push 50 次好看十倍。**节奏 > 总量**。

### 高级技巧（可选）

加这些会让 repo "活"起来：
- **GitHub Actions CI**：每次 push 跑 `mvn test` 和 `pytest`，README 顶部加个绿色 badge
- **issue 当 TODO 用**：你的 `notes/weekly/` 里的"待问列表"做成 GitHub issues，关闭它们时引用 commit
- **Discussions 区开个 "learning log"**：发周复盘，类似博客

---

## 4 · 时间线建议（从今天到 OMSCS 提交申请）

假设你目标 Fall 2027 入学（申请 deadline 通常前一年 3 月或更早）：

| 月份 | 学术 | GitHub 上的产出 |
|------|------|----------------|
| 2026-05 → 2026-08 | CS1332x 全部完成 | `cs1332-journey` 满分 progress + Python 复刻 + 30+ LeetCode |
| 2026-09 → 2026-11 | OMSCS 数学先修补全（线代、概率） | `omscs-math-refresh`：Jupyter notebook 形式，每章一个 notebook |
| 2026-12 → 2027-01 | 一门 OMSCS 推荐技术课（CS1331 Java OOP 或 CS6035 信息安全的 free 部分） | 第二个 `<course>-journey` repo |
| 2027-02 | 一个端到端项目（把金融背景 × Python ML 结合） | `<一个有故事的项目>` |
| 2027-03 | OMSCS 申请 | Profile README + SOP 引用你的 GitHub |

**OMSCS SOP 里你会写**：
> "为了系统准备 CS 研究生学习，我在 2026 年开始自学 Georgia Tech 的 CS1332x。我的完整学习过程公开在 github.com/.../cs1332-journey — 包含每周的学习复盘、Java 原始实现以及 Python 等价复刻，体现我从金融背景人士转向 CS 学习者的过程。"

这一句话 = 一个 repo 链接 = 一份非常有说服力的证据。

---

## 5 · 三种典型 repo 模板（你可以照着抄结构）

### 模板 A：学习类 repo（如本 repo）

```
xxx-journey/
├── README.md          # progress + 介绍 + 导航
├── docs/              # study method, notes
├── lectures/          # module 笔记 + 实现
├── practice/          # 习题代码
└── .gitignore
```

**信号**：自驱学习 + 长期坚持

### 模板 B：技术工具/包

```
finance-toolkit/
├── README.md          # what it does + install + usage examples + screenshots
├── pyproject.toml     # 真正的 Python 包
├── src/finance_toolkit/
├── tests/             # pytest, 覆盖率 >= 80%
├── examples/          # Jupyter notebooks 展示用法
├── .github/workflows/ # CI: pytest + lint on push
└── CHANGELOG.md       # 版本历史
```

**信号**：工程能力 + 真用户思维

### 模板 C：项目/应用

```
portfolio-optimizer/
├── README.md           # 第一屏: 截图 + "这做什么" + "为什么我做这个"
├── notebooks/01-data-exploration.ipynb
├── notebooks/02-model.ipynb
├── notebooks/03-backtest.ipynb
├── src/                # 抽出的可复用代码
├── data/               # 小样本数据（大文件用 LFS 或外链）
├── reports/            # PDF 或 HTML 报告
└── requirements.txt
```

**信号**：能从问题到结果完整交付

---

## 6 · 红线（千万不要做）

1. **不要 push 别人的代码当自己的**（招生官有反向搜索工具）
2. **不要 push 完整作业答案**（违反 GTx Honor Code → 取消证书 → 申请直接挂）
3. **不要"刷绿点"** — 写脚本自动 commit 空文件被看出来是反向减分
4. **不要 push private/敏感内容** — 客户数据、内部系统截图、API key
5. **不要在 commit message 里写脏话或私人吐槽** — 永久记录

---

## 7 · 最后一个角度：你的金融/运营背景是优势，不是包袱

很多 OMSCS 申请者是计算机本科应届生 / 转行新人。**你的差异化在于你已经在真实业务里做过事**。利用它：

- 把你过去的工作场景转化成 1 个具体项目（例如"我以前做 XX 报表，每月手动 8 小时 → 我用 Python 自动化"）
- 在 SOP 里把"我为什么想做 OMSCS"和你过去的经历缝合
- 你不需要假装是个 CS 学生 — 你是"带着商业理解的工程师候选人"

**这是录取委员会会记住的人**。

---

## 一句话总结

> 你不是在准备一份 GitHub 给招生官炫耀。你是在用学习的副产品让一个客观的事实——"我在过去 12 个月里每周都在 push 数据结构和数学的代码"——自己说话。**让事实说话，比让 SOP 说话有力 10 倍。**
