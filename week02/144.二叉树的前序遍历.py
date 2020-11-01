#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        res = []
        visited = set()
        def dfs(root,visited):
            if root in visited: return 
            visited.add(root)
            if root:
                res.append(root.val)
                dfs(root.left, visited)
                dfs(root.right, visited)
        dfs(root, visited)
        return res


        # cur, stack, res = root, [], []
        # while cur or stack:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res
        
# @lc code=end

