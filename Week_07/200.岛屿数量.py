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
# 2. union find
# class UnionFind:
#     def __init__(self, grid):
#         m, n = len(grid), len(grid[0])
#         self.count = 0
#         self.parent = [-1] * (m * n)
#         self.rank = [0] * (m * n)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     self.parent[i * n + j] = i * n + j
#                     self.count += 1

#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]

#     def union(self, x, y):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if rootx != rooty:
#             if self.rank[rootx] < self.rank[rooty]:
#                 rootx, rooty = rooty, rootx
#             self.parent[rooty] = rootx
#             if self.rank[rootx] == self.rank[rooty]:
#                 self.rank[rootx] += 1
#             self.count -= 1

#     def getCount(self):
#         return self.count

class Solution:
    def numIslands(self, grid) -> int:
        # 1. dfs
        # def helper(grid, row, col):
        #     if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or not int(grid[row][col]):
        #         return

        #     grid[row][col] = "0"
        #     helper(grid, row - 1, col)
        #     helper(grid, row, col - 1)
        #     helper(grid, row, col + 1)
        #     helper(grid, row + 1, col)

        # count = 0
        # if not grid:
        #     return count

        # for row in range(len(grid)):
        #     for col in range(len(grid[row])):
        #         if int(grid[row][col]):
        #             count += 1
        #             helper(grid, row, col)

        # return count

        # 2. union find
        # nr = len(grid)
        # if nr == 0:
        #     return 0
        # nc = len(grid[0])

        # uf = UnionFind(grid)
        # for r in range(nr):
        #     for c in range(nc):
        #         if grid[r][c] == "1":
        #             grid[r][c] = "0"
        #             for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        #                 if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
        #                     uf.union(r * nc + c, x * nc + y)

        # return uf.getCount()

        # 3. union find
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = row*col+1
        p = [i for i in range(row*col+1)]
        r = [1 for _ in range(row*col+1)]

        def find(p, i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                x = i
                i = p[i]
                p[x] = root
            return root

        def union(p, i, j):
            nonlocal count
            root_i = find(p, i)
            root_j = find(p, j)
            if root_i == root_j:
                return

            if r[root_i] > r[root_j]:
                p[root_j] = root_i
            elif r[root_i] < r[root_j]:
                p[root_i] = root_j
            else:
                p[root_i] = root_j
                r[root_j] += 1

            count -= 1

        for x in range(row):
            for y in range(col):
                if grid[x][y] == "0":
                    union(p, x*col+y, row*col)
                if grid[x][y] == "1":
                    for dir in ((0, 1), (1, 0)):
                        new_x = x + dir[0]
                        new_y = y + dir[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == "1":
                            union(p, new_x*col+new_y, x*col+y)

        return count - 1
# @lc code=end
s = Solution()
print(s.numIslands([
    ["1", "0", "1", "1", "1"],
    ["1", "0", "1", "0", "1"],
    ["1", "1", "1", "0", "1"]
    ]))
