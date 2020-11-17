#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        
        count, m = 0, len(grid)
        n = len(grid[0]) if m else 0

        def dfs(i, j):
            grid[i][j] = "0"
            for new_i, new_j in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == "1":
                    dfs(new_i, new_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        
        return count



# @lc code=end

