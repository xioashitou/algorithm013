#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (33.68%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    123.4K
# Total Submissions: 366.5K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
#
#
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
#
#
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        if not s:
            return res

        # index = len(s) - 1
        # while index > -1 and s[index] == ' ':
        #     index -= 1
        # while index > -1:
        #     if s[index] == ' ':
        #         break
        #     res += 1
        #     index -= 1
        # return res

        # s = s.strip().split()
        # if not s:
        #     return 0
        # else:
        #     return len(s[-1])

        return len(s.strip(' ').split(' ')[-1])
# @lc code=end

