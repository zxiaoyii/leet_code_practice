class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n 

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx == fy:
                return False 
            
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx

            parent[fy] = fx

            if rank[fx] == rank[fy]:
                rank[fx] += 1
            return True
        
        for a, b in edges:
            union(a, b)

        return sum(1 for i in range(n) if parent[i] == i)
        
                     
            
