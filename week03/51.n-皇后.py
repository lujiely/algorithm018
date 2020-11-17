#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n):
        col, diag, reverse_diag = [0]*n, [0]*n*2, [0]*2*n
        grid = [['.']*n for _ in range(n)]
        res = []
        def helper(depth):
            if depth == n:
                res.append([''.join(grid[i]) for i in range(n)])
                return 
            for i in range(n):
                if not col[i] and not diag[depth+i] and not reverse_diag[n-depth+i]:
                    grid[depth][i] = "Q"
                    col[i], diag[depth+i], reverse_diag[n-depth+i] = 1, 1, 1
                    helper(depth + 1)
                    grid[depth][i] = "."
                    col[i], diag[depth+i], reverse_diag[n-depth+i] = 0, 0, 0
        helper(0)
        return res
            

# @lc code=end

