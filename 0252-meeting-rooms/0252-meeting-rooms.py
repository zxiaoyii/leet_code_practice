class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        i = 1
        while i < len(intervals):
            a = intervals[i][0]
            # b = intervals[i][1]
            if a < intervals[i - 1][1]:
                return False
            i += 1
        return True