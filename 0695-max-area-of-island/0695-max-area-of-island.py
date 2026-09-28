class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        res = 0
        self.area = 0
        def dfs(i, j):
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            self.area += 1
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc)
                    
        for a in range(m):
            for b in range(n):
                if grid[a][b] == 1:
                    self.area = 0
                    dfs(a, b)
                    res = max(res, self.area)
                    
        return res
                    
