class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')
        for a, b in intervals:
            if a >= end:
                end = b
            else:
                count += 1
        return count