class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        for idx, height in stack:
            res = max(res, height * (len(heights) - idx))
        return res