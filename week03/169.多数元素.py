#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums):
        #分治
        def helper(left, right):
            if left == right:
                return nums[left]
            mid = (right - left)//2 + left
            left_ele = helper(left, mid)
            right_ele = helper(mid+1, right)
            left_count = sum(1 for i in range(left, right+1) if nums[i] == left_ele)
            right_count = sum(1 for i in range(left, right+1) if nums[i] == right_ele)
            return left_ele if left_count > right_count else right_ele
        return helper(0, len(nums)-1)
        
        
# @lc code=end

