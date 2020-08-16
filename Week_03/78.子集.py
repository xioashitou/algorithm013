#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (77.72%)
# Likes:    703
# Dislikes: 0
# Total Accepted:    118.5K
# Total Submissions: 152.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        # 1.dumb, not right
        # if not nums:
        #     return [nums]

        # def sub_set(nums):
        #     if len(nums) == 1:
        #         return [nums]

        #     subs = []
        #     s_subs = []
        #     for index in range(len(nums)):
        #         if [nums[index]] not in subs:
        #             subs.append([nums[index]])
        #         l = nums[:]
        #         l.pop(index)
        #         if l not in subs:
        #             subs.append(l)

        #         s_subs.extend(sub_set(l))

        #     subs.extend([s_sub for s_sub in s_subs if s_sub not in subs])
        #     subs.append(nums)
        #     return subs
        # res = sub_set(nums)
        # res.append([])
        # return res

        # 2.recursion
        def dfs(index, sub):
            # if not pick this index as part of sub set
            res.append(sub)
            # if pick this index as part of sub set
            for i in range(index, length):
                dfs(i + 1, sub + [nums[i]])

        res = []
        length = len(nums)
        dfs(0, [])
        return res

        # 2.1. recursion, better to understand
        # def dfs(index, sub):
        #     if index == length:
        #         res.append(sub)
        #         return

        #     # if not pick this index as part of sub set
        #     dfs(index + 1, sub)
        #     # if pick this index as part of sub set
        #     dfs(index + 1, sub + [nums[index]])

        # res = []
        # length = len(nums)
        # dfs(0, [])
        # return res

        # 3.iteration
        # res = [[]]
        # for num in nums:
        #     res = res + [[num] + sub for sub in res]
        # return res
# @lc code=end

