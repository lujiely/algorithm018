#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import collections
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        dic = collections.Counter(nums)
        heap, res = [],[]
        for i in dic:
            heapq.heappush(heap,(-dic[i], i))
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

# @lc code=end

