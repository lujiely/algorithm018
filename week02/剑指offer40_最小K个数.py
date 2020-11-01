#coding:utf-8
"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 方法一：利用sorted
        # return sorted(arr)[:k]
        
        #方法二：利用heapq
        # heapq.heapify(arr)
        # return heapq.nsmallest(k,arr)

        #方法三：大根堆
        heap = arr[:k]
        self.build_heap(heap)

        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.heapify(heap, 0)
        return heap
    
    def build_heap(self, heap):
        for i in range(len(heap)//2 - 1, -1, -1):
            self.heapify(heap, i)
    
    def heapify(self, heap, i): 
        left , right = 2*i + 1, 2*i + 2

        largest = i
        if left < len(heap) and heap[left] > heap[largest]:
            largest = left
        if right < len(heap) and heap[right] > heap[largest]:
            largest = right
        
        if largest != i:ss
            self.swap(heap, i, largest)
            self.heapify(heap, largest)
    
    def swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]

    
    # #方法一：快排
    # def getLeastNumbers01(self, arr, k):
    #     if not arr or k <= 0: return []
    #     if len(arr) <= k: return arr
    #     self.quick_sort(arr, 0, len(arr)-1)
    #     return arr[:k]
    # def quick_sort(self,arr, left, right):
    #     if left < right: 
    #         pivot = self.partition(arr, left, right)
    #         self.quick_sort(arr, left, pivot-1)
    #         self.quick_sort(arr, pivot+1, right)
    # def partition(self,arr, left, right):
    #     pivot = left 
    #     i = j = pivot + 1
    #     while j <= right:
    #         if arr[j] <= arr[pivot]:
    #             self.swap(arr, i, j)
    #             i += 1
    #         j += 1
    #     self.swap(arr, pivot, i-1)
    #     return i-1
    # def swap(nums, i, j):
    #     nums[i], nums[j] = nums[j], nums[i]

    # #方法二：归并排序
    # def getLeastNumbers02(self, arr, k):
    #     if not arr or k <= 0: return []
    #     if len(arr) <= k: return arr
    #     return self.merge_sort(arr)[:k]
    
    # def merge_sort(self, arr):
    #     if len(nums) <= 1: return nums
    #     mid = len(nums)//2
    #     left = self.merge_sort(nums[:mid])
    #     right = self.merge_sort(nums[mid:])
    #     return self.merge(left,right)
    
    # def merge(self, l1, l2):
    #     while i < len(l1) and j < len(l2):
    #         if l1[i] <= l2[j]:
    #             res.append(l1[1])
    #             i += 1
    #         else:
    #             res.append(l2[j])
    #             j += 1
    #     if i == len(l1): 
    #         res.extend(l2[j:])
    #     else:
    #         res.extend(l1[i:])
    #     return res
        
