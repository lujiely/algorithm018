#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
import  collections
import heapq
class Solution:
    def maxSlidingWindow(self, nums, k):
        # 方法一：双端队列
        # deque = collections.deque()
        # res = []
        # for i, num in enumerate(nums):
        #     if deque and deque[0] <= i - k: deque.popleft()
        #     while deque and num > nums[deque[-1]]: deque.pop()
        #     deque.append(i)
        #     if i >= k - 1:
        #         res.append(nums[deque[0]])
        # return res
        
        # 方法二：heapq
        res, heap = [], []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i + 1 >= k: 
                while heap and heap[0][1] < i + 1 - k: 
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
        

        

# @lc code=end

