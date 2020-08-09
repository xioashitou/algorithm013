#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (66.14%)
# Likes:    103
# Dislikes: 0
# Total Accepted:    26.4K
# Total Submissions: 39.9K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其层序遍历:
#
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
#
#
#
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res

        # 1、queue
        # queue = [root]
        # while queue:
        #     l = len(queue)
        #     sub = []
        #     for _  in range(l):
        #         node = queue.pop(0)
        #         sub.append(node.val)
        #         for child in node.children:
        #             if child:
        #                 queue.append(child)
        #     res.append(sub)

        # 2、optimized queue
        pre_layer = [root]
        while pre_layer:
            cur_layer = []
            res.append([])
            for node in pre_layer:
                res[-1].append(node.val)
                cur_layer.extend(node.children)  # actuallt I do not understand why extend can work
            pre_layer = cur_layer

        return res
# @lc code=end

