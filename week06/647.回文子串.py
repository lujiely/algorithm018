#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                length = i - j + 1
                if length == 1:
                    dp[j][i] = True
                    count += 1
                if length == 2 and s[i]==s[j]:
                    dp[j][i] = True
                    count += 1
                #首位相同，且去除首尾的情况下还是回文串情况
                if length > 2 and s[i]==s[j] and dp[j+1][i-1] is True:
                    dp[j][i] = True
                    count += 1
        return count




        
# @lc code=end

