#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits):
        phone = {"2":["a","b","c"],
                "3":["d","e","f"],
                "4":["g","h","i"],
                "5":["j",'k','l'],
                "6":['m','n','o'],
                "7":['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        res = []
        def helper(temp, digits):
            if len(digits) == 0:
                res.append("".join(temp))
            else:
                for letter in phone[digits[0]]:
                    helper(temp+[letter], digits[1:])
        if digits: helper([],digits)
        return res

# @lc code=end

