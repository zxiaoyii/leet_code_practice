class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = []
        n = len(intervals)
        i = 1
        res.append(intervals[0])
        while i < n:
            a, b = intervals[i][0], intervals[i][1]
            if a <= res[-1][1]:
                res[-1][0] = min(a, res[-1][0])
                res[-1][1] = max(b, res[-1][1])
            else:
                res.append(intervals[i])
            i +=1
        return res