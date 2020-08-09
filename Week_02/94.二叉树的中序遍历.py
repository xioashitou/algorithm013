#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (72.34%)
# Likes:    605
# Dislikes: 0
# Total Accepted:    206.8K
# Total Submissions: 285.8K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [1,3,2]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        # 1、recursion
        # def recursion(node):
        #     nonlocal res
        #     if not node:
        #         return
        #     recursion(node.left)
        #     res.append(node.val)
        #     recursion(node.right)

        # recursion(root)

        # 2、iteration
        stack = []
        cur_node = root
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            node = stack.pop()
            res.append(node.val)
            cur_node = node.right

        return res
# @lc code=end

