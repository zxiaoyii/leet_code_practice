class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            val_l = height[l]
            val_r = height[r]
            amount = min(val_l, val_r) * (r - l)
            res = max(res, amount)
            if val_l < val_r:
                l += 1
            else:
                r -= 1
        return res
            