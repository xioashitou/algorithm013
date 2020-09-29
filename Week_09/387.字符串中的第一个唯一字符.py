#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (47.04%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    102K
# Total Submissions: 216.6K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#
#
# 示例：
#
# s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#
#
#
#
# 提示：你可以假定该字符串只包含小写字母。
#
#
# from collections import defaultdict
from collections import Counter
# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        table = Counter(s)
        # for c in s:
        #     table[c] += 1
        for index in range(len(s)):
            if table[s[index]] == 1:
                return index
        else:
            return -1
# @lc code=end

