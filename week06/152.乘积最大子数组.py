#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums):
        maxDp = [nums[0]]
        minDp = [nums[0]]
        for i in nums[1:]:
            temp = (i, i*maxDp[-1], i*minDp[-1])
            maxDp.append(max(temp))
            minDp.append(min(temp))
        return max(maxDp)
            

# @lc code=end

