class MedianFinder:

    def __init__(self):
        self.heap_max = [] # -vals
        self.heap_min = [] # +vals

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap_min, num)
        if len(self.heap_min) > 0 and len(self.heap_max) > 0 and self.heap_min[0] < -self.heap_max[0]:
            heapq.heappush(self.heap_max, -heapq.heappop(self.heap_min))
        if len(self.heap_max) > len(self.heap_min):
            heapq.heappush(self.heap_min, -heapq.heappop(self.heap_max))
        if len(self.heap_min) > len(self.heap_max) + 1:
            heapq.heappush(self.heap_max, -heapq.heappop(self.heap_min))

    def findMedian(self) -> float:
        if len(self.heap_max) == len(self.heap_min):
            return (-self.heap_max[0] + self.heap_min[0]) / 2
        return self.heap_min[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()