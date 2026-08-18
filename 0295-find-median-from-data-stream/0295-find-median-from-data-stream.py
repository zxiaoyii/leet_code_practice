class MedianFinder:

    def __init__(self):
        self.max = [] # - values
        self.min = [] # + values
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.min, num)
        if self.max and self.min and self.min[0] < -self.max[0]:
            heapq.heappush(self.max, -heapq.heappop(self.min))
        if len(self.max) > len(self.min):
            heapq.heappush(self.min, -heapq.heappop(self.max))
        elif len(self.min) > len(self.max) + 1:
            heapq.heappush(self.max, -heapq.heappop(self.min))

    def findMedian(self) -> float:
        if len(self.max) == len(self.min):
            return (self.min[0] - self.max[0]) / 2
        return self.min[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()