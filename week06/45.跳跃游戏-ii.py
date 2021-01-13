#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

'''
# @lc code=start
class Solution:
    def jump(self, nums):
        max_position, step, end  = 0, 0, 0
        for i in range(len(nums)-1):
            max_position = max(max_position, nums[i]+i)
            if i == end:
                step += 1
                end = max_position
        return step

# @lc code=end
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    # nums = [2,1,1,1,1]
    solu = Solution()
    res = solu.jump(nums)
    print(res)


