class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)
        res = []
        while len(heap) > 1:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)
            res.append(ch1)
            res.append(ch2)
            if cnt1 + 1 < 0:
                heapq.heappush(heap, (cnt1 + 1, ch1))
            if cnt2 + 1 < 0:
                heapq.heappush(heap, (cnt2 + 1, ch2))
        
        if heap:
            cnt, ch = heap[0]
            if -cnt > 1:
                return ""
            res.append(ch)
        return ''.join(res)
