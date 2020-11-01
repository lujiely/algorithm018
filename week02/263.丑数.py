#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        for factor in [2, 3, 5]:
            while num % factor == 0 and num >0:
                num //= factor
        return num == 1
# @lc code=end

