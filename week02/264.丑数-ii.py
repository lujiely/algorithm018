#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap, seen = [], set()
        seen.add(1)
        heapq.heappush(heap, 1)
        factors = [2,3,5]
        for _ in range(n):
            cur_ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = cur_ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return cur_ugly

# @lc code=end

