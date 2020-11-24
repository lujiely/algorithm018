#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if not n: return 0
        dp = [0]*n
        max_pro = -prices[0]
        for i in range(1, n):  
            max_pro = max(dp[i-1] - prices[i], max_pro)
            dp[i] = max(dp[i-1], max_pro + prices[i] - fee)
        return dp[-1]  
# @lc code=end

