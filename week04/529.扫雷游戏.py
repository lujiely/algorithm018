#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0]) if m else 0
        directions = [[-1,0],[0,-1],[1,0],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]
        def dfs(x, y):
            if board[x][y] == "E":
                count = sum(1 for dx, dy in directions if 0 <= x+dx < m and 0 <= y+dy < n and board[x+dx][y+dy] == "M")
                if count:
                    board[x][y] = str(count)
                else:
                    board[x][y] = "B"
                    for dx, dy in directions:
                        new_x, new_y = x + dx, y+dy
                        if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == "E":
                            dfs(new_x, new_y) 
            elif board[x][y] == "M":
                board[x][y] = "X"
            
        dfs(click[0], click[1])
        return board
        
# @lc code=end

