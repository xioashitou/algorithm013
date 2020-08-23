#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.63%)
# Likes:    841
# Dislikes: 0
# Total Accepted:    171.7K
# Total Submissions: 224K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1.recursion
        # res = []
        # def helper(cur, nums):
        #     if not nums:
        #         res.append(cur)
        #         return

        #     for num in nums:
        #         new_nums = nums[:]
        #         new_nums.remove(num)
        #         helper(cur + [num], new_nums)

        # helper([], nums)
        # return res

        # 2.backtrack
        res = []
        def backtrack(path, nums):
            if not nums:
                res.append(path)
                return

            for index in range(len(nums)):
                backtrack(path + [nums[index]], nums[:index] + nums[index+1:])

        backtrack([], nums)
        return res
# @lc code=end

