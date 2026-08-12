class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            c = board[i][j]
            board[i][j] = "#"

            for dx, dy in dir:
                x = i + dx
                y = j + dy
                if dfs(x, y, idx + 1):
                    return True
            board[i][j] = c    
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

                    
