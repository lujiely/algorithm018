#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums):
        # 方法一：
        # n = len(nums)
        # if n == 0: return 0
        # if n == 1: return nums[0]
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[1], nums[0])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # return dp[-1]


        # 方法二：化简版
        prev, now = 0,0
        for i in nums:
            prev, now = now, max(prev + i, now)
        return now

# @lc code=end

