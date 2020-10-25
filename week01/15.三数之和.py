#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        
        for k in range(n-2):
            if k > 0 and nums[k] == nums[k-1]: continue
            left, right = k+1, n-1
            while left < right:
                temp_sum = nums[k] + nums[left] + nums[right]
                if temp_sum == 0:
                    res.append([nums[k],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right: left += 1
                    while nums[right] == nums[right+1] and left < right: right -= 1
                elif temp_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return res

# @lc code=end
