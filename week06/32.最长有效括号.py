#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

'''

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #方法一： 栈
        # ")()())","(()"
        stack,res = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                res = max(res, i - stack[-1])
        return res


# @lc code=end


if __name__ == '__main__':
    s = ")()())"

    s = "()("
    s = '(()'
    solu = Solution()
    res = solu.longestValidParentheses(s)
    print(res)
