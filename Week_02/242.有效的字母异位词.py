#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (60.76%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    122.1K
# Total Submissions: 200.8K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 示例 1:
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 说明:
# 你可以假设字符串只包含小写字母。
# 
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()
        return list_s == list_t
        
# @lc code=end

