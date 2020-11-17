#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #方法一:单向BFS
        # wordset = set(wordList)
        # if endWord not in wordset: return 0
        # queue = [(beginWord, 1)]
        # visited = set()
        # visited.add(beginWord)
        # while queue:
        #     word, step = queue.pop(0)
        #     if word == endWord:
        #         return step
        #     for i in range(len(word)):
        #         for j in range(26):
        #             temp = word[:i] + chr(97+j) + word[i+1:]
        #             if temp not in visited and temp in wordset:
        #                 queue.append((temp, step + 1))
        #                 visited.add(temp)
        # return 0

        #双向BFS
        wordset = set(wordList)
        if endWord not in wordset: return 0
        lqueue, rqueue = [beginWord], [endWord]
        lvisit, rvisit = set(), set()
        lvisit.add(beginWord)
        rvisit.add(endWord)
        step = 0
        while lqueue and rqueue:
            if len(lqueue) > len(rqueue):
                lqueue, rqueue = rqueue, lqueue
                lvisit, rvisit = rvisit, lvisit
            step += 1
            for _ in range(len(lqueue)):
                cur = lqueue.pop(0)
                if cur in rvisit:
                    return step
                
                for i in range(len(cur)):
                    for j in range(26):
                        temp = cur[:i] + chr(97+j) + cur[i+1:]
                        if temp not in lvisit and temp in wordset:
                            lqueue.append(temp)
                            lvisit.add(temp)
        return 0


       




        
# @lc code=end

