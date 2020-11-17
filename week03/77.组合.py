#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n, k):
        res = []
        def helper(temp, start):
            if len(temp) == k:
                res.append(temp[:])
                return
            for i in range(start, n+1):
                temp.append(i)
                helper(temp, i+1)
                temp.pop()
        helper([], 1)
        return res


# @lc code=end

