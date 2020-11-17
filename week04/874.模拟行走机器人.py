#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
# from numpy import xranges
# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        ans, x, y, di = 0, 0, 0, 0
        obstacles = set(map(tuple, obstacles))
        for cmd in commands:
            if cmd == -1: #向右转
                di = (di + 1) % 4
            elif cmd == -2: #向左转
                di = (di - 1) % 4
            else:
                for K in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x = x + dx[di]
                        y = y + dy[di]
                        ans = max(ans, x**2 + y**2)
        return ans 
        




        
# @lc code=end

