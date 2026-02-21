class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = set()
        a = set()
        m, n = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # if 0 > nr or 0 > nc or m <= nr or n <= nc:
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        #pacific
        for i in range(m):
            dfs(i, 0, p)
        for j in range(n):
            dfs(0, j, p)
        #atlantic
        for i in range(m):
            dfs(i, n - 1, a)
        for j in range(n):
            dfs(m - 1, j, a)

        return [[r, c] for r, c in p & a]


                

