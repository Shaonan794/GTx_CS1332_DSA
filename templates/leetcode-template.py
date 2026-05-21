"""
LeetCode #XXX - <Title>
难度: Easy / Medium / Hard
链接: https://leetcode.com/problems/<slug>/

关联 CS1332 主题: <例如 "Module 01 - ArrayList">
关联概念卡: [[双指针]] [[原地修改]]

────────────────────────────────────────────────
问题（自己复述，不抄原文）:
    给定一个升序排列的数组，原地删除重复元素，返回新长度。

我的思路（先想后写）:
    1. 双指针：slow 指向"已确认不重复区域"的末尾，fast 扫描。
    2. nums[fast] != nums[slow] → slow+=1, nums[slow]=nums[fast]
    3. 返回 slow + 1

复杂度:
    时间 O(n)，空间 O(1)

踩坑/学到的:
    - 第一次写成 slow 从 1 开始，边界出错。slow 从 0 开始更清晰。
    - 原地修改 = 不能用 list comprehension 重新构造。

────────────────────────────────────────────────
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


# ───────── 自测（不依赖 LeetCode judge） ─────────
if __name__ == "__main__":
    cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([], 0, []),
        ([1], 1, [1]),
    ]
    sol = Solution()
    for nums, expected_len, expected_prefix in cases:
        nums_copy = nums.copy()
        k = sol.removeDuplicates(nums_copy)
        assert k == expected_len, f"len mismatch: {k} vs {expected_len}"
        assert nums_copy[:k] == expected_prefix, f"content mismatch: {nums_copy[:k]}"
        print(f"OK: {nums} -> len={k}, prefix={nums_copy[:k]}")
    print("All tests passed.")
