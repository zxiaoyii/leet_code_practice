class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for i, p in enumerate(points):
            d = p[0] * p[0] + p[1] * p[1]
            heapq.heappush(heap, (-d, i))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for d, i in heap:
            res.append(points[i])
        return res