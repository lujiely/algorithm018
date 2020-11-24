#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def groupCount(mid):
            count, s = 0, 0
            for i in range(len(nums)):
                s += nums[i]
                if s > mid:
                    s = nums[i]
                    count += 1
                    if count > m:
                        return count
            return count + 1

        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (right - left)//2 + left
            c = groupCount(mid)
            if c > m:
                left = mid + 1
            else:
                right = mid - 1
        return left
# @lc code=end

