#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle):
        # 方法一：空间复杂度O(mn)
        # dp = triangle
        # for i in range(len(triangle)-2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + dp[i][j]
        # return dp[0][0]

        # 方法二：空间复杂度O(n)
        m = len(triangle)
        dp = triangle[m-1]
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
        return dp[0]
# @lc code=end

