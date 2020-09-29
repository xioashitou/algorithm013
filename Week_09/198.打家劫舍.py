#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (46.65%)
# Likes:    1056
# Dislikes: 0
# Total Accepted:    183.1K
# Total Submissions: 392.5K
# Testcase Example:  '[1,2,3,1]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
# 示例 2：
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # optimized
        # pre = 0
        # now = 0
        # for num in nums:
        #     pre, now = now, max(pre + num, now)
        # return now

        if len(nums) < 2:
            return 0 if not nums else nums[0]
        # 1. a[i] = max(a[i-1], nums[i]+a[i-2])
        # a = nums[:]
        # a[0] = nums[0]
        # a[1] = max(nums[0], nums[1])
        # for index in range(2, len(nums)):
        #     a[index] = max(a[index - 1], a[index] + a[index - 2])
        # return a[-1]

        # 2. optimized
        # a[i][0] = max(a[i-1][0], a[i-1][1])
        # a[i][1] = nums[i] + max(a[i-2][0], a[i-2][1])
        a = [[0, 0] for _ in range(len(nums))]
        a[0][0], a[0][1] = 0, nums[0]
        a[1][0], a[1][1] = nums[0], nums[1]
        for index in range(2, len(nums)):
            a[index][0] = max(a[index - 1][0], a[index - 1][1])
            a[index][1] = nums[index] + max(a[index - 2][0], a[index - 2][1])
        return max(a[-1][0], a[-1][1])
# @lc code=end

