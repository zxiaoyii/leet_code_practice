class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h2, num)
        heapq.heappush(self.h1, -heapq.heappop(self.h2))
        if len(self.h2) + 1 < len(self.h1):
            heapq.heappush(self.h2, -heapq.heappop(self.h1))

    def findMedian(self) -> float:
        if len(self.h1) == len(self.h2):
            return (-self.h1[0] + self.h2[0]) / 2
        else:
            return -self.h1[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()