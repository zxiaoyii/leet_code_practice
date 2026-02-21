class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x[0])
        s, e = intervals[0]
        for start, end in intervals[1:]:
            if start < e:
                return False
            e = end
        return True