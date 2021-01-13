#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums):
        #[4,5,6,0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        left, right = 0, len(nums)-1
        minNum = float("inf")
        while left <= right:
            mid = (right - left)//2 + left
            if nums[mid] <= minNum:
                minNum = nums[mid]
            
          
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return minNum
# @lc code=end

