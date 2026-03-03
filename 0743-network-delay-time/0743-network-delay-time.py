class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 1:
            return 0
        
        # model the graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        # dijkstra
        heap = [(0, k)]
        visited = set()
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for w, v in graph[node]:
                new_d = w + dist
                if new_d > distance[v]:
                    continue
                distance[v] = new_d
                heapq.heappush(heap, (new_d, v))
        res = 0
        for d in distance[1:]:
            if d == float('inf'):
                return -1
            res = max(res, d)
        return res