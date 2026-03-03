class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = 0
        fresh = 0
        queue = deque([])
        dirs = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten += 1
                    queue.append((i, j))
        if fresh == 0:
            return 0
        if rotten == 0:
            return -1

        # bfs
        while queue:
            res += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dr, dc in dirs:
                    nr, nd = i + dr, j + dc
                    if 0 <= nr < m and 0 <= nd < n and grid[nr][nd] == 1:
                        grid[nr][nd] = 2
                        queue.append((nr, nd))
                        fresh -= 1
                
        if fresh > 0:
            return -1
        else:
            return res - 1
                        

        

        
        
                