#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        left, right = 0, m * n - 1
        while left <= right:
            mid = (right - left)//2 + left
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# @lc code=end

