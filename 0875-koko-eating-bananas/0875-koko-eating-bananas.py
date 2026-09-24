class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum((p + k - 1) // k for p in piles) #向上取整
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if hours_needed(mid) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        
