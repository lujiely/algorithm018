#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        res = []
        def helper(temp, left, right):
            if len(temp) == 2*n:
                res.append(temp)
                return 
            if left < n:
                helper(temp + "(", left + 1, right)
            if right < left:
                helper(temp + ")", left, right + 1)
            
            
        helper("", 0, 0)
        return res

        
        
# @lc code=end

