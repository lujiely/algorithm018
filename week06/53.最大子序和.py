#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [nums[0]] + [0] * (n-1)
        for i in range(1, n):
            dp[i] = max(0, dp[i-1]) + nums[i]
        return max(dp)


# @lc code=end

