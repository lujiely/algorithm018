#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
import collections
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordset: return []
        res, layer = [], {}
        layer[beginWord] = [[beginWord]]
        while layer:
            newLayer = collections.defaultdict(list) 
            for word in layer:
                if word == endWord:
                    res.extend(k for k in layer[word])
                else:
                    for i in range(len(beginWord)):
                        for j in range(26):
                            temp = word[:i] + chr(j+97) + word[i+1:]
                            if temp in wordset:
                                newLayer[temp] += [k + [temp] for k in layer[word]]
            wordset -= set(newLayer.keys())
            layer = newLayer
        return res


        

# @lc code=end

