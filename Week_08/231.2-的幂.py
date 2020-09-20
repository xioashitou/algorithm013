#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (48.60%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    79.4K
# Total Submissions: 163.4K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # count = 0
        # while n > 0:
        #     count += 1
        #     n &= (n - 1)
        # return count == 1

        return bin(n).count('1') == 1
# @lc code=end

