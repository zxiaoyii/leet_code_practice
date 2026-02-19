class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, index):
            if index == len(word):
                return True
            if 0 <= r < m and 0 <= c < n and board[r][c] == word[index]:
                ch = board[r][c]
                board[r][c] = "#"
                for a, b in dir:
                    if dfs(r + a, c + b, index + 1):
                        return True
                board[r][c] = ch
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False    
