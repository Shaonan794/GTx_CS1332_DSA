---
tags: [cs1332, <topic>, <data-structure-or-algorithm>]
created: {{date}}
status: seedling   # seedling | growing | evergreen
source: CS1332x Module XX
---

# <概念名 — 用一句陈述句，不要用问句>

## 这是什么（30 秒能讲完的版本）

一句话定义。例子：
> ArrayList 是基于动态数组实现的可变长度序列，提供 O(1) 索引访问和均摊 O(1) 的尾部插入。

## 为什么存在（它解决了什么问题）

如果没有它，世界会怎样？

> 原生数组定长，要扩容必须手动拷贝。ArrayList 把"扩容 + 拷贝"封装成自动行为，让调用者不再操心容量。

## 一个最小可运行例子

```java
ArrayList<Integer> list = new ArrayList<>();
list.add(1);
list.add(2);
list.get(0);   // 1
```

```python
# Python 等价
lst = []
lst.append(1)
lst.append(2)
lst[0]   # 1
```

## 关键性质 / 不变量

- 索引访问 O(1)
- 尾部插入 amortized O(1)（扩容时 O(n)）
- 中间插入 O(n)（要平移）

## 容易混淆 / 反直觉的点

- 不是 "插入永远 O(1)" — 是 **均摊** O(1)。第一次扩容那一次是 O(n)。
- `ArrayList.remove(Object)` vs `remove(int index)` 在 `<Integer>` 类型下会撞车。

## 链接到其他卡

- 上位概念：[[List ADT]]
- 同级概念：[[LinkedList]]、[[ArrayDeque]]
- 应用：[[动态规划记忆化数组]]、[[算法题中的原地修改]]
- 反例 / 对照：[[何时该用 LinkedList 而不是 ArrayList]]

## 我是怎么验证我真懂的（费曼测试）

向一个不懂编程的人解释：……（写下来。如果写不出来，回去重学。）

## 引用 / 出处

- CS1332x Module 01, Lecture 1.3
- Sedgewick *Algorithms* 4th ed., §1.3
- CLRS §10.2
