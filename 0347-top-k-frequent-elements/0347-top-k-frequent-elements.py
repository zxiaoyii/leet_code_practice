class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key in freq.keys():
            heapq.heappush(heap, (-freq[key], key))
        res = []
        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
        return res