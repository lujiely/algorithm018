#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quiMul(N):
            if N == 0: return 1
            y = quiMul(N//2)
            return y*y if N%2==0 else y*y*x
        return quiMul(n) if n >= 0 else 1./quiMul(-n)

# @lc code=end

