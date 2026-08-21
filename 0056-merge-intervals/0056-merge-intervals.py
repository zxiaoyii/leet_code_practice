class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])
        for s, e in intervals[1:]:
            e1 = res[-1][1]
            if s <= e1:
                res[-1][1] = max(e1, e)
            else:
                res.append([s, e])
        return res


            