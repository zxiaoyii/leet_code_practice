class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        
        def _dfs(i, j):
            if grid[i][j] != "1":
                return 
            grid[i][j] = "#"
            for dr, dc in dirs:
                nr, nc = dr + i, dc + j
                if 0 <= nr < m and 0 <= nc < n:
                    _dfs(nr, nc)
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    _dfs(i, j)
        return res
        