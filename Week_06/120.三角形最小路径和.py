#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (66.68%)
# Likes:    581
# Dislikes: 0
# Total Accepted:    104.3K
# Total Submissions: 156.4K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
#
#
#
# 例如，给定三角形：
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
#
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
#
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 1. dp
        # dp = triangle
        # for row in range(len(triangle) - 2, -1, -1):
        #     for col in range(len(triangle[row])):
        #         dp[row][col] += min(dp[row + 1][col], dp[row + 1][col + 1])
        # return dp[0][0]

        # 2. optimized dp
        res = triangle[-1]
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                res[col] = min(res[col], res[col + 1]) + triangle[row][col]
        return res[0]
# @lc code=end

