#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        # dp[0][0] = 1
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if matrix[i-1][j-1] == "1" else 0
                res = max(res, dp[i][j])
        return res**2
        

# @lc code=end

