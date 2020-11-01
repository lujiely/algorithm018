#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #方法一：
        # return collections.Counter(s) == collections.Counter(t)

        #方法二：
        # set_s = set(s)
        if set(t) == set(s):
            for i in set(s):
                if s.count(i) != t.count(i): return False
            return True
        return False

       


        #方法三：
        # return True if sorted(s) == sorted(t) else False
                    
        

# @lc code=end

