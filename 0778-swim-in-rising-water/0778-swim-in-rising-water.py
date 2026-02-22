class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)] #max elevation on path, row, col
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            t, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == n - 1 and c == n - 1: #reach the end
                return t
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    next_t = max(t, grid[nr][nc])
                    heapq.heappush(heap, (next_t, nr, nc))
        return -1