#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (74.46%)
# Likes:    330
# Dislikes: 0
# Total Accepted:    68.2K
# Total Submissions: 91.6K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1.recursion, backtracking
        # res = []
        # def helper(level, sub):
        #     nonlocal res
        #     if len(sub) == k:
        #         res.append(sub)
        #         return

        #     for num in range(level, n + 1):
        #         helper(num + 1, sub + [num])

        # helper(1, [])
        # return res

        # 2.
        # 尽管方法二的时间复杂度与方法一相同，但方法二却要快上许多。
        # 这是由于方法一需要处理递归调用栈，且其带来的影响在Python中比在Java中更为显著。
        nums = list(range(1, k + 1)) + [n + 1]

        output, j = [], 0
        while j < k:
            output.append(nums[:k])
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return output
# @lc code=end

