class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for a, b in intervals:
            if a <= res[-1][1]:
                res[-1][1] = max(b, res[-1][1])
            else:
                res.append([a, b])
        return res