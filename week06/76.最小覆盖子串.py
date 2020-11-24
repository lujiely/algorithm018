#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        l, ans = 0,  ""
        n = 0 #当前满足t中字母的种树
        for r, val in enumerate(s):
            if val not in counter:
                continue
            counter[val] -= 1
            if counter[val] == 0:
                n += 1
            
            while s[l] not in counter or counter[s[l]] < 0:
                if s[l] in counter: counter[s[l]] += 1
                l += 1

            if n == len(counter):
                if not ans or len(ans) > r - l + 1:
                    ans = s[l:r+1]
        return ans





# @lc code=end

