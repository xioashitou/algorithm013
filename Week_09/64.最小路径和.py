#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (67.53%)
# Likes:    675
# Dislikes: 0
# Total Accepted:    146.6K
# Total Submissions: 217.1K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#
#
from math import inf
# @lc code=start

class Solution:
    def minPathSum(self, grid) -> int:
        if not grid:
            return 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row or col:
                    up = grid[row - 1][col] if row - 1 > -1 else inf
                    left = grid[row][col - 1] if col - 1 > -1 else inf
                    grid[row][col] += min(up, left)
        return grid[-1][-1]
# @lc code=end

