class MedianFinder:
    
    def __init__(self):
        self.h1 = [] #- maxheap
        self.h2 = [] #+ minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h2, num)
        if self.h1 and self.h2 and self.h2[0] < -self.h1[0]:
            heapq.heappush(self.h1, -heapq.heappop(self.h2))
        if len(self.h1) > len(self.h2):
            heapq.heappush(self.h2, -heapq.heappop(self.h1))
        elif len(self.h2) > len(self.h1) + 1:
            heapq.heappush(self.h1, -heapq.heappop(self.h2))



    def findMedian(self) -> float:
        if len(self.h1) == len(self.h2):
            mid = (-self.h1[0] + self.h2[0]) / 2
            return mid
        else:
            return self.h2[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()