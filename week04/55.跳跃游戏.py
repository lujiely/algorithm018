#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        last = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last == 0

# @lc code=end

