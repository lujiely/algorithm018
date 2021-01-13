#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid):
        start = end = None
        m = len(grid)
        n = len(grid[0]) if m else 0
        visited = [[False]*n for i in range(m)]
        self.res, countZero = 0, 1
        for i in range (m):
            for j in range(n):
                if grid[i][j] == 1:
                    x,y = i,j
                elif grid[i][j] == 0:
                    countZero += 1
        def dfs(i, j, countZero):
            if grid[i][j] == 2 and countZero == 0:
                self.res += 1
                return 
            visited[i][j] = True
            countZero -= 1
            for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] >= 0:
                    dfs(x,y,countZero)
            visited[i][j] = False
        dfs(x,y,countZero)
        return self.res


        
# @lc code=end

