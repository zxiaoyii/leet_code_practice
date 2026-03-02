class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if grid[i][j] != '1':
                return
            grid[i][j] = '#'

            for dr, dc in dirs:
                nr, nc  = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res