#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices)s:
        n = len(prices)
        if not n: return 0
        dp = [0]*n #每只股票 收益的最大值
        max_pro = -prices[0] #初始收益
        for i in range(1,n):
            max_pro = max(dp[i-2]-prices[i], max_pro) #保证（现有增益，与买股票后收益）的最大值，因为有冷冻期，选择前前一天的最大收益
            dp[i] = max(dp[i-1], max_pro + prices[i]) #当前这个价格的最大收益是 前一天
        return dp[-1]

# @lc code=end

