#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (64.24%)
# Likes:    698
# Dislikes: 0
# Total Accepted:    200.5K
# Total Submissions: 312K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#
#

# @lc code=start
class Solution:
    def majorityElement(self, nums) -> int:
        # 1. dumb
        # table = {}
        # for num in nums:
        #     if num in table:
        #         table[num] += 1
        #     else:
        #         table[num] = 1

        # for num, count in table.items():
        #     if count > len(nums) // 2:
        #         return num

        # 2. sort, damn!!!
        # nums.sort()
        # return nums[len(nums) // 2]

        # 3. quick sort
        # def partition(nums, begin, end):
        #     pivot = nums[end]
        #     mark = begin
        #     for index in range(begin, end):
        #         if nums[index] < pivot:
        #             nums[mark], nums[index] = nums[index], nums[mark]
        #             mark += 1

        #     nums[mark], nums[end] = nums[end], nums[mark]
        #     return mark

        # l = len(nums)
        # mid = l // 2
        # begin, end = 0, l - 1
        # index = partition(nums, 0, l - 1)
        # while index != mid:
        #     if index < mid:
        #         begin = index + 1
        #         index = partition(nums, begin, end)
        #     else:
        #         end = index - 1
        #         index = partition(nums, begin, end)

        # return nums[mid]

        # 4. not change nums
        res = nums[0]
        times = 1

        for num in nums[1:]:
            if times == 0:
                times = 1
                res = num
            elif num == res:
                times += 1
            else:
                times -= 1

        return res
# @lc code=end
s = Solution()
print(s.majorityElement([3,3,4]))
