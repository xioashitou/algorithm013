#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
# https://leetcode-cn.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (28.29%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    7K
# Total Submissions: 24.6K
# Testcase Example:  '[1,3,2,3,1]'
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
# 你需要返回给定数组中的重要翻转对的数量。
#
# 示例 1:
#
#
# 输入: [1,3,2,3,1]
# 输出: 2
#
#
# 示例 2:
#
#
# 输入: [2,4,3,5,1]
# 输出: 3
#
#
# 注意:
#
#
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
#
#
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def merge_sort(nums, left, right):
            if left >= right:
                return 0

            mid = left + (right - left) // 2
            count = merge_sort(nums, left, mid) + merge_sort(nums, mid + 1, right)

            temp = []
            t, l = left, left
            for r in range(mid + 1, right + 1):
                while t <= mid and nums[t] <= 2 * nums[r]:
                    t += 1
                while l <= mid and nums[l] < nums[r]:
                    temp.append(nums[l])
                    l += 1
                temp.append(nums[r])
                count += mid - t + 1

            while l <= mid:
                temp.append(nums[l])
                l += 1

            nums[left:right + 1] = temp
            return count

        return merge_sort(nums, 0, len(nums) - 1)
# @lc code=end

