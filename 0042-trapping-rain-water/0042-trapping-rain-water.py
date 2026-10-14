class Solution:
    def trap(self, height: list[int]) -> int:
        # if n < 3 no water
        n = len(height)
        if n < 3:
            return 0
        # res = height of water - height of bar
        # height of water = min(max left height, max right height)
        l = 0 
        r = n - 1
        max_l = 0
        max_r = 0
        res = 0
        while l < r:
            max_l = max(max_l, height[l]) 
            max_r = max(max_r, height[r])
            if max_l < max_r:
                water = max_l - height[l]
                l += 1  
            else:
                water = max_r - height[r]
                r -= 1         
            if water > 0:
                res += water
        return res
            
        
        