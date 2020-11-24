#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not n: return 0
        dp = [[0]*n for i in range(3)]
        for k in range(1, 3):
            pre_max = -prices[0]
            for i in range(1, n):
                pre_max = max(dp[k-1][i-1] - prices[i], pre_max)
                dp[k][i] = max(dp[k][i-1], pre_max + prices[i])
        return dp[-1][-1]
# @lc code=end

