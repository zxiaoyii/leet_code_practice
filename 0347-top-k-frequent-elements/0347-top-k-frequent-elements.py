class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        
        for key, val in c.items():
            heapq.heappush(h, (val, key))
            if len(h) > k:
                heapq.heappop(h)
        
        return [key for val, key in h]
        
        