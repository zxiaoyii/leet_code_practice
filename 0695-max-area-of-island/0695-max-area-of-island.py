class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # area = 0
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                self.area += 1
                grid[r][c] = 0
                for dr, dc in dir:
                    dfs(dr + r, dc + c)

        
        for i in range(m):
            for j in range(n):
                self.area = 0
                if grid[i][j] == 1:
                    dfs(i, j)
                    res = max(res, self.area)
        return res