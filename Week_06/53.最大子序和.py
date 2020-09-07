#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (52.21%)
# Likes:    2381
# Dislikes: 0
# Total Accepted:    317.2K
# Total Submissions: 607.3K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # f[i] = max(f[i-1], 0) + a[i]
        dp = nums
        for index in range(1, len(nums)):
            dp[index] = max(0, dp[index - 1]) + nums[index]
        return max(dp)
# @lc code=end

