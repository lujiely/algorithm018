#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"{":"}", "[":"]", "(":")"}
        stack = []
        for char in s:
            if char in dict:
                stack.append(char)
            else:
                if len(stack)== 0 or char != dict[stack.pop()]:
                    return False
        return False if stack else True

            
        



# @lc code=end

