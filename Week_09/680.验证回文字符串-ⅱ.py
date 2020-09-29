#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.84%)
# Likes:    265
# Dislikes: 0
# Total Accepted:    52.8K
# Total Submissions: 132.6K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
#
#
# 输入: "aba"
# 输出: True
#
#
# 示例 2:
#
#
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#
#
# 注意:
#
#
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
#
#
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True

        count = 0
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                if count == 0:
                    if left + 1 <= right and s[left + 1] == s[right]:
                        left += 1
                        count += 1
                    elif left <= right - 1 and s[left] == s[right - 1]:
                        right -= 1
                        count += 1
                    else:
                        return False
                else:
                    return False
            left += 1
            right -= 1
        return True
# @lc code=end

