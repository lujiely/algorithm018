#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    import collections
    def levelOrder(self, root):
        # #方法一：BFS
        res = []
        def bfs(root):
            queue = []
            queue.append(root)
            while queue:
                curVal = []
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    if not node: continue
                    curVal.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                if curVal: res.append(curVal)
        bfs(root)
        return res


        #方法二：
        # res = []
        # def dfs(root, level):
        #     if not root:
        #         return 
        #     if len(res) == level: 
        #         res.append([])
        #     res[level].append(root.val)
        #     if root.left:
        #         dfs(root.left, level+1) 
        #     if root.right:
        #         dfs(root.right, level+1)
        # dfs(root, 0)
        # return res



# @lc code=end

