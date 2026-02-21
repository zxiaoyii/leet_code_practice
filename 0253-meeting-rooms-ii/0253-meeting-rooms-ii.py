class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #sort the intervals by its start time
        intervals.sort()
        #minheap to put all the end time
        heap = []
        res = 0
        #traverse the intervals 
            #if the start time is bigger or = than the heap[0]
                #use the conference room
            #else 
                #add room by one
        for s, e in intervals:
            if heap and s >= heap[0]:
                heapq.heapreplace(heap, e)
            else:
                heapq.heappush(heap, e)
                res += 1
        #return the room num
        return res
        