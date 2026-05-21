# Git + GitHub 配置与推送指南

> 假设你 Git 用过一点但不熟，目标是 30 分钟内把这个 repo 推上 GitHub，并建立一套你能坚持几个月的日常工作流。

## 0 · 你今天要完成的 4 件事

1. 验证 / 配置 Git（5 分钟）
2. 生成 SSH key 并加到 GitHub（10 分钟）
3. 在 GitHub 创建 repo 并把本地内容 push 上去（10 分钟）
4. 学会日常工作流：`add → commit → push`（5 分钟）

完成后你就有一个公开的、活的、招生官能看到的 repo。

---

## 1 · 验证 Git 配置（5 分钟）

打开终端（macOS: Terminal.app 或 iTerm；Windows: Git Bash），运行：

```bash
git --version            # 应该 >= 2.30
git config --global user.name "Shaonan"          # 改成你的名字
git config --global user.email "yzwsn2024@gmail.com"
git config --global init.defaultBranch main      # 默认分支用 main
git config --global pull.rebase false            # pull 默认用 merge，新手更安全
git config --global core.autocrlf input          # macOS/Linux；Windows 用 true
```

**重要**：这里的 email **必须**和你 GitHub 账号验证的 email 一致，否则你的 commit 在 GitHub 上不会显示成"你"的（不会有头像、不计入贡献日历）。如果你的 GitHub 用了 noreply 邮箱（隐私设置），用 GitHub 提供的 `XXXX+username@users.noreply.github.com` 形式。

验证：
```bash
git config --global --list | grep -E "user|init|pull"
```

---

## 2 · SSH key（推荐）vs HTTPS（备选）

两种 push 方式都能用。**推荐 SSH** — 一次配好，之后再也不用输密码或 token。

### 2A · 生成 SSH key

```bash
ssh-keygen -t ed25519 -C "yzwsn2024@gmail.com"
# 一路回车，passphrase 可以留空（图省事）或设一个（更安全）
```

把公钥复制到剪贴板：

```bash
# macOS
pbcopy < ~/.ssh/id_ed25519.pub

# Linux
xclip -sel clip < ~/.ssh/id_ed25519.pub

# Windows (Git Bash)
clip < ~/.ssh/id_ed25519.pub
```

### 2B · 加到 GitHub

1. 浏览器打开 https://github.com/settings/keys
2. 点 **"New SSH key"**
3. Title 写 `Shaonan MacBook 2026`（或任何你能认得的名字）
4. Key 框里粘贴（Ctrl/Cmd + V）
5. **Add SSH key**

### 2C · 验证

```bash
ssh -T git@github.com
# 第一次会问 "Are you sure you want to continue connecting" → yes
# 然后应该看到：Hi <你的 username>! You've successfully authenticated...
```

看到 "successfully authenticated" 就完成了。

---

## 3 · 在 GitHub 上创建 repo（不要勾选 README）

1. https://github.com/new
2. **Repository name**: `cs1332-journey`
3. **Description**: `My journey through GTx CS1332x — Data Structures & Algorithms, with Java implementations and Python equivalents.`
4. **Public**（OMSCS 招生角度，必须公开）
5. **不要勾选** Initialize with README / .gitignore / license（我们本地已经有了）
6. **Create repository**

GitHub 会给你一个空 repo 页面，里面有 "…or push an existing repository" 的命令 — 这就是下一步。

---

## 4 · 把本地 repo push 上去（关键 10 分钟）

打开终端，**cd 到本仓库目录**。本会话里我把内容生成在了我的临时文件夹（你看不到），所以**你需要先把它复制到你的电脑上**。两种方式：

### 方式 A：让我直接保存到你电脑的一个文件夹

回一句"帮我把 cs1332-journey 文件夹放到我电脑的 ~/Projects/"，我会请求你授权一个目录然后写过去。

### 方式 B：从这次会话的链接下载

我会在最后给你 `computer://` 链接 — 点击后文件会出现在你的下载位置，然后你把整个文件夹移到你想要的地方，例如 `~/Projects/cs1332-journey`。

### 之后（无论 A 还是 B 都一样）：

```bash
cd ~/Projects/cs1332-journey        # 改成你实际的路径

git init                            # 初始化为 git 仓库
git add .                           # 把所有文件加入暂存区
git status                          # 看一眼，确认 .gitignore 在工作（不应看到 .DS_Store 等）

git commit -m "chore: initial scaffold — CS1332x learning journey

- README with learning plan and progress tracker
- docs/ with study method, git guide, portfolio strategy
- templates/ for module / weekly / leetcode notes
- obsidian-vault/ for Zettelkasten concept cards
- .gitignore for Java + Python + IDE artifacts"

git branch -M main                  # 确保主分支叫 main
git remote add origin git@github.com:<你的 username>/cs1332-journey.git
git push -u origin main             # 第一次 push，-u 记住 upstream
```

**期望输出**：一段进度条 + `branch 'main' set up to track 'origin/main'`. 

刷新 GitHub 页面 — 你应该能看到文件树和 README 渲染。

> 如果报 `Permission denied (publickey)` → 回 §2C 重新检查 SSH key。
> 如果报 `remote: Repository not found` → 检查 §3 创建的 repo 名字和 §4 命令里的 username 是否一致。

---

## 5 · 日常工作流（你之后 99% 的时间在做这个）

```bash
# 1. 改了/加了文件之后
git status                                  # 看改了什么
git diff                                    # 看具体改了哪些行

# 2. 加入暂存
git add lectures/module-01-arrays/notes.md   # 加特定文件（推荐）
# 或
git add .                                    # 加所有（小心！会包含你不想提交的）

# 3. commit
git commit -m "notes(module-01): finish ArrayList complexity analysis"

# 4. push
git push
```

完事。三行命令。

### Commit message 规范（我推荐你用，招生官会注意到）

格式：`<type>(<scope>): <短描述>`

| type | 用法 |
|------|------|
| `feat` | 新功能、新实现（如 `feat(module-04): implement BST insertion`） |
| `fix` | 修 bug（`fix(arraylist): off-by-one in remove(i)`） |
| `notes` | 学习笔记（`notes(module-02): linked list traversal patterns`） |
| `test` | 加/改测试（`test(heap): boundary cases for sift-down`） |
| `docs` | 文档（`docs(readme): update progress tracker`） |
| `refactor` | 重构（不改行为）（`refactor(quicksort): extract partition fn`） |
| `chore` | 杂项（`chore: bump python to 3.12`） |
| `wip` | Work in progress（**慎用** — 推上 main 不好看） |

**好的 commit message**：
```
feat(module-05): implement min-heap with sift-up/sift-down

- Array-backed binary heap (1-indexed for cleaner parent/child math)
- O(log n) insert / removeMin
- JUnit tests cover: empty, single element, ascending insert,
  descending insert, duplicates, capacity boundary
```

**差的 commit message**：
```
update
fix stuff
asdf
WIP
```

---

## 6 · 分支策略（轻量级，适合个人学习 repo）

对学习仓库，简化版分支策略：

- `main` — 永远可"展示给招生官"的状态。绿色测试、内容连贯。
- `module-XX-wip` — 学一个新 module 时建一个分支。乱写、试错、刷题都在这里。
- 学完一个 module → squash merge 到 main（用一个干净的 commit 进 main）

```bash
git checkout -b module-04-trees                  # 开始 module 04
# ... 一周内任意 commit、push、试错 ...
git push -u origin module-04-trees

# 学完后回到 main 合并
git checkout main
git merge --squash module-04-trees
git commit -m "feat(module-04): complete BST + tree traversal"
git push
git branch -d module-04-trees                    # 删本地分支
git push origin --delete module-04-trees         # 删远程分支
```

这样 main 的历史是干净的"每个 commit = 一个 module"，招生官点开 commit graph 一眼能看懂你的进度。

> 如果觉得这套太复杂，前两周就在 main 上直接干，等手熟了再加分支。**比起完美工作流，更重要的是每天 push 一次。**

---

## 7 · 一个 "Codespaces" 的备选（如果你想云端写）

如果你想偶尔在没有 Java 环境的机器上学：
1. 在 GitHub repo 页面按 `.`（点号）→ 直接打开网页版 VS Code 编辑
2. 或者 **Code → Codespaces → Create codespace** → 浏览器里有完整 Java + Python 环境（每月 60 小时免费）

适合通勤路上、咖啡馆、用别人电脑时。

---

## 8 · 隐私和学术诚信再次提醒

**绝对不要 push 的东西**：
- edX 完整作业答案（违反 Honor Code，可能被取消证书）
- 含有同学姓名、邮箱、Discord 截图的笔记
- 你的私人 SSH key（`~/.ssh/id_ed25519` 不带 `.pub` 的那个）
- 任何 `.env` 文件、API key、密码

我已经在 `.gitignore` 里排除了 `assignments/*/solution.*` 等模式。但每次 `git add` 之前看一眼 `git status` 是好习惯。

如果不小心 push 了敏感内容：
```bash
# 立刻删除并改写历史（破坏性！）
git rm --cached <文件路径>
git commit -m "chore: remove sensitive file"
git push --force-with-lease

# 但请假定该内容已被外界看到。如果是 API key，立刻去对应服务作废。
```

---

## 9 · 推荐的 IDE / 工具配置

- **VS Code** + 扩展：Java Extension Pack, Python, Pylance, GitLens, GitHub Copilot（学生可申请免费）
- **IntelliJ IDEA Community Edition**：写 Java 时体验最好
- **GitHub CLI** (`brew install gh`)：让 PR / issue 在终端搞定
- **lazygit** (`brew install lazygit`)：可视化 git，比命令行直观

---

## 10 · 排错清单（按报错信息查）

| 报错 | 原因 | 解法 |
|------|------|------|
| `Permission denied (publickey)` | SSH key 未加 / 加错 | 回 §2 重做 |
| `Updates were rejected` | 远程比你新 | `git pull --rebase` 然后再 push |
| `failed to push some refs` | 同上 | 同上 |
| `fatal: refusing to merge unrelated histories` | 第一次 push 时远程不空 | `git pull origin main --allow-unrelated-histories` |
| `The file will have its original line endings...` | CRLF 警告（Windows） | 通常无害；用 §1 里的 `core.autocrlf` 配置 |
| `Your branch is ahead of 'origin/main' by N commits` | 本地有 N 个未推送 commit | `git push` |
| `nothing to commit, working tree clean` | 没有改动 | 正常 — 没东西要 commit |

---

## 一句话总结

**第一周强迫自己每天 push 一次**（哪怕 commit 只是 `notes: add 3 lines about complexity`）。习惯一旦养成，剩下的就是顺势而为。两个月后你的贡献日历会变成深绿色 — 那就是给招生官看的"我能坚持"。
