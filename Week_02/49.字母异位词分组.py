#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (62.87%)
# Likes:    416
# Dislikes: 0
# Total Accepted:    93.2K
# Total Submissions: 148.1K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#
import collections
# @lc code=start
class Solution:
    def groupAnagrams(self, strs):
        if len(strs) < 2:
            return [strs]

        # res = collections.defaultdict(list)
        # for s in strs:
        #     key_list = [0] * 26
        #     for c in s:
        #         key_list[ord(c)-ord('a')] += 1
        #     res[tuple(key_list)].append(s)
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())
# @lc code=end

