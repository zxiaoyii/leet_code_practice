class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        res = 0
        def dfs(i, j):
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n :
                    dfs(nr, nc)
            return 

        for a in range(m):
            for b in range(n):
                if grid[a][b] == '1':
                    dfs(a, b)
                    res += 1
        return res
                    
