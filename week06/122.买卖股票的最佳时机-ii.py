#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        #方法一：允许买卖 很多次， 化简版
        # max_profit = 0
        # for i in range(1, len(prices)):
        #     max_profit += max(0, prices[i] - prices[i-1])
        # return max_profit

        #方法一：允许买卖 很多次， 通用版 超时
        # n = len(prices)
        # if not n: return 0
        # dp = [[0]*n for i in range(k+1)] #k=n+1 允许买卖 n 次
        # for t in range(1, k+1):
        #     pre_max = -prices[0]
        #     for i in range(1, n):
        #         pre_max = max(dp[t-1][i-1] - prices[i], pre_max)
        #         dp[t][i] = max(dp[t][i-1], pre_max + prices[i])
        # return dp[-1][-1]

        #方法一：允许买卖 很多次，化简通用版本
        n = len(prices)
        if not n: return 0
        dp = [0 for i in range(n)] #k=n+1 允许买卖 n 次
        pre_max = - prices[0]
        for i in range(1, n):
            pre_max = max(dp[i-1] - prices[i], pre_max)
            dp[i] = max(dp[i-1], pre_max + prices[i])
        return dp[-1]

        
# @lc code=end

