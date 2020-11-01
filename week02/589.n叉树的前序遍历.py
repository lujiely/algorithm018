#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root):

        # 方法一：递归
        # res = []
        # visited = set()
        # def dfs(root, visited):
            # if root in visited: return
            # visited.add(root)
        #     if root:
        #         res.append(root.val)
        #         for i in root.children:
                    # if i not in visited: 
        #               dfs(i)
        #     return res
        # dfs(root, visited)
        # return res

        # 方法二：迭代
        if not root: return []
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children[::-1])
        return res


# @lc code=end

