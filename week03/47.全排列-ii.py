#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, temp):
            visited = set()
            if not len(nums):
                # if temp[:] not in res:
                res.append(temp[:])
                return 
            for i in range(len(nums)):
                if nums[i] in visited: continue
                helper(nums[:i]+nums[i+1:], temp+[nums[i]])
                visited.add(nums[i])

        helper(nums, [])
        return res

# @lc code=end

