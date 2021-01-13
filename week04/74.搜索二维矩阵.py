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

        #方法二：
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        if not n: return False
        for i in range(m):
            if target > matrix[i][-1]:
                continue
            else:
                left = 0
                right = n
                while left <= right:
                    mid = (right - left)//2 + left
                    if target == matrix[i][mid]:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

        return False
# @lc code=end

