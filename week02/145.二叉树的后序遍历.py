#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        # res = []
        # visited = set()
        # def dfs(root, visited):
            # if root in visited: return 
            # visited.add(root)
        #     if root:
        #         dfs(root.left, visited)
        #         dfs(root.right, visited)
        #         res.append(root.val)
        # dfs(root, visited)
        # return res


        cur, stack, res = root, [], []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]


        
# @lc code=end

