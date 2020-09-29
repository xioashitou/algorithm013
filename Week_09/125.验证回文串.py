#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (46.43%)
# Likes:    278
# Dislikes: 0
# Total Accepted:    165.8K
# Total Submissions: 357.1K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
#
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        temp = ""
        for c in s:
            if c.isalnum():
                temp += c.lower()
        # if not temp:
        #     return True

        # left, right = 0, len(temp) - 1
        # while left <= right:
        #     if temp[left].lower() != temp[right].lower():
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        return temp == temp[::-1]
# @lc code=end

