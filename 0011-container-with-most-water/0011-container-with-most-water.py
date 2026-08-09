class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            a = height[l]
            b = height[r]
            area = min(a, b) * (r - l)
            res = max(res, area)
            if a > b:
                r -= 1
            else:
                l += 1
        return res