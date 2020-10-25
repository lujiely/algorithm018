#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"{":"}","[":"]","(":")"}
        res = []
        for char in s:
            if char in dict:
                res.append(char)
            elif len(res)==0 or dict[res.pop()] != char:
                return False
        return False if res else True
                


# @lc code=end

