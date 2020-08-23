#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (40.90%)
# Likes:    785
# Dislikes: 0
# Total Accepted:    144.4K
# Total Submissions: 353K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
#
#
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#
#
#

# @lc code=start
class Solution:
    def canJump(self, nums) -> bool:
        # 1. recursion, expired
        # res = False

        # def helper(nums, index):
        #     nonlocal res
        #     if index == len(nums) -1:
        #         res = True
        #         return

        #     for i in range(1, nums[index] + 1):
        #         if res or index + i >= len(nums):
        #             return
        #         helper(nums, index + i)

        # helper(nums, 0)
        # return res

        # 2. greed, right to left
        # if not nums:
        #     return False

        # reachable = len(nums) - 1
        # for i in range(len(nums) - 1, -1, -1):
        #     if i + nums[i] >= reachable:
        #         reachable = i

        # return reachable == 0

        # 2. greed, left to right
        reachable = 0
        for index, num in enumerate(nums):
            if index <= reachable:
                reachable = max(index + num, reachable)
        return reachable >= len(nums) - 1

# @lc code=end

s = Solution()
print(s.canJump([2,1,1]))
