class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. don't have circle
        # 2. n nodes, n - 1 edges

        if len(edges) != n - 1:
            return False
        
        parent = list(range(n)) 
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: #have the same root , and if add this edge, will be circle
                return False 
            if rank[px] < rank[py]:
                px, py = py, px

            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
        return True



        

