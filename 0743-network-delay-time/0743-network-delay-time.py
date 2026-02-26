from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # model the graph
        graph = defaultdict(list) # u ->[(w, v), (...), ...]
        for u, v, w in times:
            graph[u].append((w, v))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        # dijkstra 
        heap = [(0, k)] # distance -> node
        
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for w, v in graph[node]:
                new_d = d + w
                if new_d < dist[v]:
                    dist[v] = new_d
                    heapq.heappush(heap, (new_d, v))
                    
        res = float('-inf')          
        for i in range(1, n + 1):
            val = dist[i]
            if val == float('inf'):
                return -1
            else:
                res = max(res, val)
        return res
                
        
            
        
        
        
        
        
        