class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            for dr, dc in dirs:
                nr, nc = dr + i, dc + j
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == word[idx]:
                    c = board[nr][nc]
                    board[nr][nc] = '#'
                    if dfs(nr, nc, idx + 1):
                        return True
                    board[nr][nc] = c

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if dfs(i, j, 1):
                        return True
                    board[i][j] = word[0]
        return False

        
            