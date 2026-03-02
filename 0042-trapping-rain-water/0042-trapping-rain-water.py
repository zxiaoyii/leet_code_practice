class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        res = 0
        max_left = 0
        max_right = 0
        l = 0 
        r = len(height) - 1

        while l <= r:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            if max_left < max_right:
                amount = min(max_left, max_right) - height[l]
                if amount > 0:
                    res += amount
                l += 1    
            else:
                amount = min(max_left, max_right) - height[r]
                if amount > 0:
                    res += amount
                r -= 1
        return res
            
            