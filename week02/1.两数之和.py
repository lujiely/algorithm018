#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [i, dict[target-num]]
            dict[num] = i


#  @lc code=end
