#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums):
        res = []
        def helper(nums, temp):
            if not nums:
                res.append(temp[:])
                return 
            for i in range(len(nums)):
                helper(nums[:i] + nums[i+1:], temp+[nums[i]])
        helper(nums, [])
        return res
# @lc code=end

