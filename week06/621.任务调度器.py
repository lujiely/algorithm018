#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
import collections
class Solution:
    def leastInterval(self, tasks, n):
        length = len(tasks)
        counter = collections.Counter(tasks)
        max_task_count = max(counter.values())
        res = (max_task_count - 1) * (n + 1)
        for item in counter.items():
            if item[1] == max_task_count:
                res += 1
        return res if res >= length else length

# @lc code=end

