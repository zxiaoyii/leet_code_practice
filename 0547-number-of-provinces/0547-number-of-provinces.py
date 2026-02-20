class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return sum(1 for i in range(n) if find(i) == i)