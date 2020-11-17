#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = [(start, 0)]
        possible = ["A","C","G","T"]
        while queue:
            (word, step)= queue.pop(0)
            if word == end:
                return step
            for i  in range(len(word)):
                for p in possible:
                    temp = word[:i] + p + word[i+1:]
                    if temp in bank:
                        bank.remove(temp)
                        queue.append((temp, step+1))
        return -1

# @lc code=end

