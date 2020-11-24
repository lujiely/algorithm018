#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums):
        def helper(nums):
            if not nums: return 0
            n = len(nums)
            if n == 1: return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            return dp[-1]
        return max(helper(nums[:-1]), helper(nums[1:])) if len(nums) != 1 else nums[0]

# @lc code=end

