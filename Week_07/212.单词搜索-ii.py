#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (42.62%)
# Likes:    233
# Dislikes: 0
# Total Accepted:    20.7K
# Total Submissions: 48.6K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
# '["oath","pea","eat","rain"]'
#
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
# 示例:
#
# 输入:
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
#
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
#
# 提示:
#
#
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
# 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
#
#
#
from collections import defaultdict
# @lc code=start
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
END_OF_WORD = '#'
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        res = set()
        # build trie
        root = defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        def dfs(board, row, col, cur_word, cur_dict):
            nonlocal res
            cur_word += board[row][col]
            cur_dict = cur_dict[board[row][col]]
            if END_OF_WORD in cur_dict:
                res.add(cur_word)

            tmp, board[row][col] = board[row][col], '@'
            for i in range(4):
                x, y = row + dx[i], col + dy[i]
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != '@' and board[x][y] in cur_dict:
                    dfs(board, x, y, cur_word, cur_dict)
            board[row][col] = tmp

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in root:
                    dfs(board, row, col, '', root)
        return list(res)
# @lc code=end

