#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
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
    def postorder(self, root):
        # 方法一:递归
        # res = []
        # visited = set()
        # def dfs(root, visited):
            # if root not in visited: return
            # visited.add(root)
        #     if root:
        #         for i in root.children:
                    # if i not in visited:
        #               dfs(i)
        #         res.append(root.val)
        #     return res
        # dfs(root, visited)
        # return res

        # 方法二：迭代
        if not root: return []
        stack, res = [root], []
        while stack:
            p = stack.pop()
            res.append(p.val)
            stack.extend(p.children)        
        return res[::-1]


        
# @lc code=end

