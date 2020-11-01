#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root):
        if not root: return []
        stack, res = [root], []
        while stack:
            cur_layer, cur_value = [], []
            for node in stack:
                cur_value.append(node.val)
                cur_layer.extend(node.children)
            stack = cur_layer
            res.append(cur_value)
        return res
        
# @lc code=end

