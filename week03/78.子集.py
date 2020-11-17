#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []
        def helper(temp, start):
            res.append(temp[:])
            for i in range(start, n):
                # temp.append(nums[i])
                helper(temp+[nums[i]], i + 1)
        helper([], 0)
        return res

            
# @lc code=end

