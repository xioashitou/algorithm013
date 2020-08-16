#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (32.07%)
# Likes:    713
# Dislikes: 0
# Total Accepted:    156.5K
# Total Submissions: 487.5K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
#
#
#
import math
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 1.recursion
        # res = True
        # def helper(node, lower, upper):
        #     nonlocal res
        #     if not node:
        #         return

        #     if node.val <= lower or node.val >= upper:
        #         res = False
        #         return

        #     helper(node.left, lower, node.val)
        #     helper(node.right, node.val, upper)

        # helper(root, -math.inf, math.inf)
        # return res

        # 2. iteration, in-order
        elements = []
        stack = []
        cur_node = root
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            node = stack.pop()
            if elements and node.val <= elements[-1]:
                return False
            elements.append(node.val)
            cur_node = node.right

        return True
# @lc code=end

