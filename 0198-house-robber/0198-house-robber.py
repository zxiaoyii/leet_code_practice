class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0

        res = 0
        for i, n in enumerate(nums):
            res = max(p1 + n, p2) 
            p1 = p2 
            p2 = res 
        return res
        

