#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#
# https://leetcode-cn.com/problems/to-lower-case/description/
#
# algorithms
# Easy (75.82%)
# Likes:    133
# Dislikes: 0
# Total Accepted:    53.9K
# Total Submissions: 71.1K
# Testcase Example:  '"Hello"'
#
# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
#
#
#
# 示例 1：
#
#
# 输入: "Hello"
# 输出: "hello"
#
# 示例 2：
#
#
# 输入: "here"
# 输出: "here"
#
# 示例 3：
#
#
# 输入: "LOVELY"
# 输出: "lovely"
#
#
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        # return str.lower()

        # res = ""
        # if not str:
        #     return res

        # offset = ord('a') - ord('A')
        # for ch in str:
        #     if 'A' <= ch <= 'Z':
        #         ch = chr(ord(ch) + offset)
        #     res += ch
        # return res
# @lc code=end

