# Day 1 行动清单（按顺序做，预计 90 分钟）

> 这份清单不是"了解一下"，是今晚就要做完的事。做完它，你就从"想学"变成"开始学"。

## ⏱ 0 · 准备（5 分钟）

- [ ] 准备 1 杯水、1 个不振动的角落、关掉手机通知
- [ ] 打开终端 + 浏览器
- [ ] 创建你的本地工作目录，例如 `mkdir -p ~/Projects && cd ~/Projects`

## ⏱ 1 · 把这份脚手架放到你电脑（10 分钟）

两种方式选一种：

**A. 让 Claude 直接帮你写到你电脑的某个文件夹**
回复一句"帮我把 cs1332-journey 写到我电脑的 ~/Projects/"

**B. 自己下载**
点最终消息里的 `computer://` 链接，把 `cs1332-journey/` 整个文件夹移到 `~/Projects/`

之后：
```bash
cd ~/Projects/cs1332-journey
ls -la         # 应该看到 README.md, .gitignore, docs/, lectures/ 等
```

## ⏱ 2 · 注册 / 准备 GitHub 账号（10 分钟，已有就跳）

- [ ] https://github.com 注册（如果还没账号）
- [ ] 设头像、名字、bio（"Finance background, learning CS for OMSCS"）
- [ ] Settings → Emails → 添加你的真实邮箱并验证

## ⏱ 3 · 跟着 `docs/git-github-guide.md` 走完 §1 到 §5（30 分钟）

打开 `docs/git-github-guide.md`，逐步做：
- [ ] §1：配置 `git config`
- [ ] §2：生成 SSH key 并加到 GitHub
- [ ] §3：创建 `cs1332-journey` repo（**公开**）
- [ ] §4：本地 init + add + commit + push

第一次 push 成功后**刷新 GitHub 页面**，看到 README 渲染 → 你完成了今天最大的成就。

## ⏱ 4 · 注册 edX 并 enroll CS1332xI（10 分钟）

- [ ] 打开 https://www.edx.org/course/data-structures-algorithms-i
- [ ] 注册 edX 账号（如果还没有）
- [ ] **Audit 模式免费可以学**，**Verified Track 约 $200 拿证书**
  - OMSCS 申请目的：**建议买证书**，写在简历和 SOP 里更有说服力
  - 但你也可以先 audit 学 2 周，确认能坚持再付费
- [ ] Enroll 之后浏览一下 syllabus，记下 Module 列表 → 回去更新 README 里的进度表

## ⏱ 5 · 把 Obsidian Vault 关联（10 分钟，可选今天）

- [ ] 下载 Obsidian https://obsidian.md
- [ ] Open folder as vault → 选 `cs1332-journey/obsidian-vault/`
- [ ] 安装两个插件（Community Plugins）：
  - **Templater**：用模板加速概念卡创建
  - **Spaced Repetition**：把卡片转成 Anki 风格的间隔重复
- [ ] 打开 `MOCs/CS1332-MOC.md` 看一眼整体地图

## ⏱ 6 · 写下你的承诺（5 分钟）

新建 `notes/weekly/week-00-kickoff.md`，写：

```markdown
# Week 00 — Kickoff (YYYY-MM-DD)

## 我承诺什么

- 每周学习时间：__ 小时
- 一周里我固定能学的时段：周__、周__、周__（具体时间段）
- 我会在每周日 ___ 点做复盘
- 目标完成日期：CS1332 全部 module → YYYY-MM-DD

## 我为什么学这门课

（写 3 句你自己的真心话 — 不是给招生官看的，是给三个月后想放弃的自己看的）

1. 
2. 
3. 

## 我能预见的最大障碍

- 
- 

## 第一周（下周）我会做什么

- 看 Module 01 视频
- 完成 Java ArrayList 实现
- 写 Python 复刻
- 完成 5 道 LeetCode（题目: 26, 27, 88, 283, 977）
- 周日复盘
```

commit + push 这个文件：

```bash
git add notes/weekly/week-00-kickoff.md
git commit -m "notes(week-00): kickoff commitment"
git push
```

## ⏱ 7 · 完成（5 分钟庆祝）

- [ ] 截一张 GitHub repo 主页的图发给朋友 / 自己存下来 — 这是 "before" 照片
- [ ] 在日历上加一个**今天起每周日晚 8 点**的"复盘"提醒，重复 12 周
- [ ] 关电脑

---

## 明天起的节奏

读 `docs/study-method.md` §1 的周表 — 那是接下来 12 周你的默认日程。

**最重要的两条**：
1. 每天 push 一次（哪怕只是一行笔记）
2. 周日不复盘 = 这周白学

加油 Shaonan，OMSCS 见。
