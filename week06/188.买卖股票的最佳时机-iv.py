#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices):
        n = len(prices)
        if not n: return 0
        dp = [[0]*n for _ in range(k + 1)]
        for t in range(1, k+1):
            max_pro = -prices[0]
            for i in range(1, n):
                max_pro = max(dp[t-1][i-1] - prices[i], max_pro)
                dp[t][i] = max(dp[t][i-1], max_pro + prices[i])
        return dp[-1][-1] 
# @lc code=end

