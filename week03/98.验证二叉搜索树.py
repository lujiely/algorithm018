#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        def helper(root, maxval=float("inf"), minval=float('-inf')):
            if not root: return True
            if not(minval < root.val < maxval): return False
            return helper(root.left, root.val, minval) and helper(root.right, maxval, root.val)
        return helper(root)


       


# @lc code=end

