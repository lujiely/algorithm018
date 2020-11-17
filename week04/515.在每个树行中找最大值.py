#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        res = []
        def bfs(root):
            queue = [root]
            while queue:
                maxVal = -2**31
                # curVal = []
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    if not node: continue
                    # curVal.append(node.val)
                    if node.val > maxVal:
                        maxVal = node.val
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                # if curVal:
                #     curVal.sort()
                #     res.append(curVal[-1])
                res.append(maxVal)
        if root: bfs(root)
        return res
        



        
# @lc code=end

