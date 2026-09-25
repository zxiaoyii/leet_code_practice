class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, b - a)
        return -heap[0] if heap else 0
