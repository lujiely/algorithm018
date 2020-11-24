#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [0]*(n+1)
        dp[0] = 1 #辅助
        dp[1] = 1 #一个台阶需要一步
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2] #[1,2]
        return dp[-1]

        

        



# @lc code=end

