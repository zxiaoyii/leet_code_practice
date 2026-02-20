class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        edge_nodes = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "A"
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1: #on the edge
                        edge_nodes.append((i, j))
                        
    
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and board[r][c] == "A":
                board[r][c] = "O"
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    dfs(nr, nc) 
            return

        for r, c in edge_nodes:
            dfs(r, c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "X"
        


        
            


