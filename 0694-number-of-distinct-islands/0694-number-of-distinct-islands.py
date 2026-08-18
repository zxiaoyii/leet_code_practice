class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c, direction):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return ""
            if grid[r][c] == 0:
                return ""
            
            grid[r][c] = 0  # 标记已访问（原地修改）
            path = direction
            path += dfs(r + 1, c, 'D')
            path += dfs(r - 1, c, 'U')
            path += dfs(r, c + 1, 'R')
            path += dfs(r, c - 1, 'L')
            path += '#'       # 回溯标记
            return path
        
        shapes = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    shape = dfs(i, j, 'S')
                    shapes.add(shape)
        
        return len(shapes)