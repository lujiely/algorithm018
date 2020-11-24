#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        res = float("-inf")
        for left in range(n):
            sums = [0] * m
            for right in range(left, n):
                for i in range(m):
                    sums[i] += matrix[i][right]
                lst = [0]
                cur = 0
                for num in sums:
                    cur += num
                    loc = bisect.bisect_left(lst, cur-k)
                    if loc < len(lst):
                        res = max(cur-lst[loc], res)
                    bisect.insort(lst, cur)
        return res


        
# @lc code=end

