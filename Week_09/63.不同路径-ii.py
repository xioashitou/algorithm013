#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (36.75%)
# Likes:    413
# Dislikes: 0
# Total Accepted:    101.9K
# Total Submissions: 277.2K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
#
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#
#
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[1] + [0] * (col - 1)] + [[0] * col for _ in range(row - 1)]
        for m in range(row):
            for n in range(col):
                if obstacleGrid[m][n]:
                    dp[m][n] = 0
                else:
                    dp[m][n] += (dp[m - 1][n] if m - 1 > -1 else 0) + \
                        (dp[m][n - 1] if n - 1 > -1 else 0)
        return dp[-1][-1]
# @lc code=end

