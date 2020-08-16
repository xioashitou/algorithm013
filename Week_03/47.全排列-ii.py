#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (59.58%)
# Likes:    373
# Dislikes: 0
# Total Accepted:    80K
# Total Submissions: 134.2K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 1. dumb, recursion
        # res = []
        # def helper(cur, nums):
        #     nonlocal res
        #     if not nums and cur not in res:
        #         res.append(cur)
        #         return

        #     for num in nums:
        #         new_nums = nums[:]
        #         new_nums.remove(num)
        #         helper(cur + [num], new_nums)

        # helper([], nums)
        # return res

        # 2.optimized recursion
        res = []
        def helper(cur, nums):
            nonlocal res
            if not nums:
                res.append(cur)
                return

            used = []
            for num in nums:
                if num in used:
                    continue
                used.append(num)
                new_nums = nums[:]
                new_nums.remove(num)
                helper(cur + [num], new_nums)

        helper([], nums)
        return res
# @lc code=end

