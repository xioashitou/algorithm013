#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.11%)
# Likes:    724
# Dislikes: 0
# Total Accepted:    146K
# Total Submissions: 291.3K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1:
#
# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(grid, row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or not int(grid[row][col]):
                return

            grid[row][col] = "0"
            helper(grid, row - 1, col)
            helper(grid, row, col - 1)
            helper(grid, row, col + 1)
            helper(grid, row + 1, col)

        count = 0
        if not grid:
            return count

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if int(grid[row][col]):
                    count += 1
                    helper(grid, row, col)

        return count
# @lc code=end

