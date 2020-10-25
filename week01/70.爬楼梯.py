#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        if n == 1: return 1
        if n == 2: return 2
        dp[1], dp[2] = 1, 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]



# @lc code=end

