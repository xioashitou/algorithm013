#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (75.95%)
# Likes:    1226
# Dislikes: 0
# Total Accepted:    161.6K
# Total Submissions: 212.7K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例：
#
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
#
#
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        if not n:
            return [""]

        res = []
        def generator(left, right, max, s):
            if left == max and right == max:
                res.append(s)
                return

            if left < max:
                generator(left + 1, right, max, s + '(')
            if right < max and right < left:
                generator(left, right + 1, max, s + ')')

        generator(0, 0, n, '')
        return res
# @lc code=end

s = Solution()
print(s.generateParenthesis(1))