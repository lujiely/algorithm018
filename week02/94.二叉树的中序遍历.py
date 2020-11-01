#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        #方法一：递归一：
        # if not root: return []
        #中序遍历
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # 前序遍历
        # return  [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right)
        # 后序遍历
        # return  self.inorderTraversal(root.left) + self.inorderTraversal(root.right) + [root.val]

        # 递归二:前中后序递归模板
        # visited = set()
        # def dfs(root, visited):
            # if root in visited: return 
            # visited.add(root)
        #     if root: 
        #     #中序遍历
            #     dfs(root.left, visited)
            #     res.append(root.val)
            #     dfs(root.right, visited)

        #     #前序遍历
        #     # res.append(root.val)
        #     # dfs(root.left, visited)
        #     # dfs(root.right, visited)

        #     #前序遍历
        #     # dfs(root.left, visited)
        #     # dfs(root.right, visited)
        #     # res.append(root.val)
        # res = []
        # dfs(root, visited)
        # return res

        #迭代1：前中后序迭代模板
        stack, cur, res = [], root, []
        #中序模板
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    #     # 前序模板1：
    #     while stack or cur:
    #         while cur:
    #             res.append(cur.val)
    #             stack.append(cur)
    #             cur = cur.left
    #         cur = stack.pop()
    #         cur = cur.right

    #     #后序模板：
    #     while stack or cur:
    #         while cur:
    #             res.append(cur.val)
    #             stack.append(cur.right)
    #             cur = cur.right
    #         cur = stack.pop()
    #         cur = cur.left
    #     return res[::-1]


    #     #前中后层次标记法
    #     stack, res = [(0, root)], []
    #     while stack:
    #         flag, cur = stack.pop()
    #         if not cur: continue
    #         if flag == 0:
    #             #前序标记
    #             stack.append((0, cur.right))
    #             stack.append((0, cur.left))
    #             stack.append((1, cur))

    #             #中序标记
    #             stack.append((0, cur.right))
    #             stack.append((1, cur))
    #             stack.append((0, cur.left))

    #             #后序标记
    #             stack.append((1, cur))
    #             stack.append((0, cur.right))
    #             stack.append((0, cur.left))
    #         else:
    #             res.append(cur.val)
    #     return res
            



    # def levelOrder(self, root):
    #     #方法一：
    #     if not root: return []
    #     stack, res = [root], []
    #     while stack:
    #         layer, layer_value = [],[]
    #         for node in stack:
    #             layer_value.append(node.val)
    #             if node.left: layer.append(node.left)
    #             if node.right: layer.append(node.right)
    #         stack = layer
    #         res.append(layer_value)
    #     return res

    #     #方法二：层序标记法
    #     queue, res = [(0, root)], [] #队列先进先出
    #     while queue:
    #         flag, cur = queue.pop(0)
    #         if not cur: continue
    #         if flag == 0:
    #             #层序遍历这三个顺序无所谓，因为是队列，只弹出队首
    #             queue.append((1, cur))
    #             queue.append((0, cur.left))
    #             queue.append((0,cur.right))
    #         else:
    #             res.append(cur.val)
    #     return res








        
# @lc code=end

