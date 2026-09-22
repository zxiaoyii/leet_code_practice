class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 1
        intervals.sort()
        heap = []
        res = 0
        for s, e in intervals:
            if heap and s >= heap[0]:
                heapq.heapreplace(heap, e)
            else:
                heapq.heappush(heap, e)
                res += 1
        return res
