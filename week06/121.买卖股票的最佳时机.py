#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        # 方法一： 空间复杂度O(1)
        # max_profit = 0
        # min_profit = int(1e9)
        # for price in prices:
        #     max_profit = max(max_profit, price - min_profit)
        #     min_profit = min(min_profit, price)

        # #方法二：空间复杂度O(n)
        # n = len(prices)
        # if not n: return 0
        # dp = [0] * n
        # min_profit = int(1e9)
        # for i in range(n):
        #     min_profit = min(min_profit, prices[i])
        #     dp[i] = max(prices[i] - min_profit, dp[i-1])
        # return dp[-1]

        #通用方法：允许买卖 k 多次的方法
        n = len(prices)
        if not n: return 0
        dp = [[0]*n for i in range(2)] #k=2 允许买卖 k-1次
        for k in range(1, 2):
            pre_max = -prices[0]
            for i in range(1, n):
                pre_max = max(dp[k-1][i-1] - prices[i], pre_max)
                dp[k][i] = max(dp[k][i-1], pre_max + prices[i])
        return dp[-1][-1]


# @lc code=end

