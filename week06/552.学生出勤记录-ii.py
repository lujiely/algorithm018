#
# @lc app=leetcode.cn id=552 lang=python3
#
# [552] 学生出勤记录 II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        MaxValue = 1000000007
        dp = [0]*6 if n <= 5 else [0] * (n + 1) 
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        dp[3] = 7
        for i in range(4, n+1):
            dp[i] = ((dp[i-1]*2)%MaxValue + (MaxValue - dp[i-4]))%MaxValue
        
        sumn = dp[n]
        for i in range(1, n+1):
            sumn += (dp[i-1]*dp[n-i])%MaxValue
        
        return int(sumn%MaxValue)


        
# @lc code=end

