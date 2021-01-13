#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
class Solution:
    def canCross(self, stones):
        '''
             0,     1,   3,     5,    7,    6,    8,    12,    17
        0,  False  True  False False False False False  False  False
        1,  True   True  True  False False False False  False  False
        3,  False  True  True  True  True  False False  False  False
        5,  False  False False False False False False  False  False
        6,  False  False False False False False False  False  False
        8,  False  False False False False False False  False  False
        12, False  False False False False False False  False  False
        17, False  False False False False False False  False  False                    
        '''
        n = len(stones)
        dp = [[False]*n for _ in range(n)]
        dp[0][1] = True
        for i in range(1, n):
            for j in range(i-1,-1,-1):
                dist = stones[i] - stones[j]
                if dist > i:
                    break
                if dp[j][dist]:
                    if i == n-1:
                        return True
                    dp[i][dist] = dp[i][dist-1] = dp[i][dist+1] = True
        return False




        # @lc code=end

