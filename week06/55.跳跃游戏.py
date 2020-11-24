#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums):
        index = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= index:
                index = i
        return index == 0



# @lc code=end

