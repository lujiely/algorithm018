#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        max_area = 0
        left, right = 0, len(height)-1
        while left < right:
            area = (right - left)*min(height[left], height[right])
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


# @lc code=end
