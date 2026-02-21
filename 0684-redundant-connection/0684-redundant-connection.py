class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
    
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            fa, fb = find(a), find(b)
            if fa == fb:
                return False
            if rank[fa] < rank[fb]:
                fa, fb = fb, fa
            parent[fb] = fa
            if rank[fa] == rank[fb]:
               rank[fa] += 1
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]
        return []



        