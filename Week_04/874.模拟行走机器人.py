#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
# https://leetcode-cn.com/problems/walking-robot-simulation/description/
#
# algorithms
# Easy (37.47%)
# Likes:    105
# Dislikes: 0
# Total Accepted:    10.5K
# Total Submissions: 28.1K
# Testcase Example:  '[4,-1,3]\n[]'
#
# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
#
#
# -2：向左转 90 度
# -1：向右转 90 度
# 1 <= x <= 9：向前移动 x 个单位长度
#
#
# 在网格上有一些格子被视为障碍物。
#
# 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
#
# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
#
# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。
#
#
#
# 示例 1：
#
# 输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
#
#
# 示例 2：
#
# 输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#
#
#
#
# 提示：
#
#
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# 答案保证小于 2 ^ 31
#
#
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_dis = 0

        X, Y = False, True
        axis_table = {X: 0, Y: 0}  # True means x-axis coordinate, False means y-axis coordinate
        axis = Y  # dir default to y-axis coordinate

        NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3  # direction
        dir_table = {NORTH: 1, EAST: 1, SOUTH: -1, WEST: -1}
        direc = NORTH

        # ! trun list to set, or it will cause a timeout ! #
        obstacles = set(map(tuple, obstacles))

        for command in commands:
            if command < 0:
                axis = not axis
                direc = (direc + 1) % 4 if command == -1 else (direc + 3) % 4
                continue

            for _ in range(command):
                axis_table[axis] += dir_table[direc]
                if (axis_table[X],axis_table[Y]) in obstacles:
                    axis_table[axis] -= dir_table[direc]
                    break
                max_dis = max(max_dis, sum([x * x for x in axis_table.values()]))

        return max_dis
# @lc code=end

