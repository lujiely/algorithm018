#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount, tenCount = 0, 0
        for bil in bills:
            if bil == 5:
                fiveCount += 1
            elif bil == 10:
                fiveCount, tenCount = fiveCount - 1, tenCount + 1
            elif tenCount > 0: fiveCount, tenCount = fiveCount - 1, tenCount -1
            else: fiveCount -= 3
            if fiveCount < 0: return False
        return True

        
# @lc code=end

