#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # 方法一:动态规划简化版，空间复杂度O(n)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if m else 0
        cur = [1]+[0] * n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    cur[j] += cur[j-1]
                else:
                    cur[j] = 0
        return cur[-2]
        
        
        # #方法二： 动态规划基础版 时间复杂度O(mn),空间复杂度O(mn)
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0]) if m else 0
        
        # #初始化条件
        # dp = [[0]*n for _ in range(m)]
        # if obstacleGrid[0][0] == 0: dp[0][0] = 1 
        # for i in range(1, m):
        #     if obstacleGrid[i][0] == 0:
        #         dp[i][0] = dp[i-1][0]
        # for j in range(1, n):
        #     if obstacleGrid[0][j] == 0:
        #         dp[0][j] = dp[0][j-1]
        
        # #动态方程建立
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if obstacleGrid[i][j] == 0:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        #         else:
        #             dp[i][j] = 0
        # return dp[-1][-1]
# @lc code=end

