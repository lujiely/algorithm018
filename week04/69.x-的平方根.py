#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, 0
        while left <= right:
            mid = (right - left)//2 + left
            if mid**2 <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans 


# @lc code=end

