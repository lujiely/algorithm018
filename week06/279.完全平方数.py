#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
import math
class Solution:
    def numSquares(self, n):
        #转换成最少硬币数
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        dp = [float("inf")]*(n + 1)
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = min(dp[i-square] if i-square>=0 else float("inf") for square in squares) + 1
        return dp[-1]

        
        

# @lc code=end

