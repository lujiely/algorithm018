#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0]) if m else 0
        dp = grid
        for i in range(m):
            for j in range(n):
                if i==j==0: continue
                elif i == 0: dp[i][j] += dp[i][j-1]
                elif j == 0: dp[i][j] += dp[i-1][j]
                else: dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
# @lc code=end

