#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (38.72%)
# Likes:    1245
# Dislikes: 0
# Total Accepted:    350.6K
# Total Submissions: 905.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # if not strs:
        #     return res
        # strs.sort(key=lambda x: len(x))

        # for index in range(len(strs[0])):
        #     c = strs[0][index]
        #     for sub in strs:
        #         if c != sub[index]:
        #             return res
        #     res += c
        # return res

        if not strs:
            return ""

        # for i in range(len(strs[0])):
        #     c = strs[0][i]
        #     for j in range(len(strs)):
        #         if i >= len(strs[j]) or strs[j][i] != c:
        #             return strs[0][:i]
        # return strs[0]

        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1
# @lc code=end

