#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums):
        end, step, max_position = 0, 0, 0
        for i in range(len(nums)-1):
            max_position = max(nums[i]+i, max_position)
            if i == end:
                step += 1
                end = max_position
        return step



# @lc code=end

