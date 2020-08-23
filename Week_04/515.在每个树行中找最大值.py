#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (61.00%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    14.9K
# Total Submissions: 24.4K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
#
# 示例：
#
#
# 输入:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \
# ⁠     5   3   9
#
# 输出: [1, 3, 9]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        pre_layer = [root]
        while pre_layer:
            res.append(pre_layer[0].val)
            cur_layer = []
            for node in pre_layer:
                res[-1] = max(res[-1], node.val)
                if node.left:
                    cur_layer.append(node.left)
                if node.right:
                    cur_layer.append(node.right)
            pre_layer = cur_layer

        return res
# @lc code=end

