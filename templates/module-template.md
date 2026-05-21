# Module XX — <主题，例如 "ArrayList"> 

> 学习日期：YYYY-MM-DD → YYYY-MM-DD · 用时：X 小时

## 1 · 我能用一句话回答的核心问题

学完这一周，我必须能不看任何资料回答："**<本周的核心问题，例如：ArrayList 和原生数组的本质区别、增删的均摊复杂度推导，以及它什么时候不该用？>**"

## 2 · 核心概念地图

按重要程度递减列。每个概念要 **(a)** 自己复述定义，**(b)** 给一个一句话例子。

- **<概念 A，例如 "动态数组"**：……（自己的话）
- **<概念 B>**：……

## 3 · 关键 API / 操作复杂度

| 操作 | 最好 | 平均 | 最坏 | 备注 |
|------|------|------|------|------|
| `add(item)` | O(1) | O(1) amortized | O(n) | 触发扩容时是 O(n) |
| `add(i, item)` | | | | |
| `remove(i)` | | | | |
| `get(i)` | | | | |
| `contains(item)` | | | | |

## 4 · Java 实现要点（边写边记的"踩坑日记"）

写代码时遇到的具体困惑，记在这里。例子：
- `Object[]` vs 泛型 `T[]` 的协变陷阱：……
- 何时 throw `IndexOutOfBoundsException` vs `IllegalArgumentException`：……
- 测试时发现 `equals()` 用 `==` 比较对象引用 → 改用 `.equals()`：……

## 5 · Python 复刻 — 同样的逻辑、不同的语言

> 写在 `python-equivalents/module-XX/`

**Python 里"等价物"是什么？**

- Java `ArrayList<T>` ↔ Python `list`（CPython 底层就是动态数组）
- 但 Python `list` 多了 slicing、负索引、列表推导 → 我自己实现时**故意不用**这些，强迫自己理解底层

**复刻时学到的新东西**：
- ……

## 6 · LeetCode 联动（3-5 道）

| 题号 | 标题 | 难度 | 我的解法 | 第一次能否独立解出 | 用时 |
|------|------|------|----------|--------------------|------|
| 26 | Remove Duplicates from Sorted Array | Easy | 双指针 | ✅ | 12 min |
| 27 | Remove Element | Easy | 双指针 | ✅ | 6 min |
| 88 | Merge Sorted Array | Easy | 从后往前 | ❌ 第二次 | 25 min |

> 题解代码：`practice/leetcode/<题号>-<slug>.py`

## 7 · 主动回忆问题（一周后自己问自己）

写 5 个可以一周后用来抽考自己的问题。答案**不要**写在这里 — 答案在你脑子里，否则就回去重学。

1. ArrayList 扩容时为什么是 2 倍而不是 1.5 倍或 3 倍？trade-off 是什么？
2. 如果 `remove(0)` 是 O(n)，那为什么生产代码里还经常用 ArrayList？
3. ……

## 8 · 还没搞懂的地方（诚实记录）

- [ ] ……
- [ ] ……

> 这些标 ❓ 的点是下一次 office hours / Discord / Stack Overflow 的提问清单。

## 9 · 链接到 Obsidian 概念卡片

学完这一节后，把上面"核心概念"拆成原子卡片，放到 `obsidian-vault/concepts/`：

- [[ArrayList 均摊分析]]
- [[Java 泛型数组创建限制]]
- [[动态数组扩容策略]]

---

**复盘提示**：完成本 module 后，把第 1 节的"一句话回答"录一段 1 分钟语音解释给自己听（费曼技巧）。如果讲不流畅，回去补 5、7、8 节。
