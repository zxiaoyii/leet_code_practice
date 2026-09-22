class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0
        for p in prices:
            res = max(res, p - min_price)
            min_price = min(min_price, p)
        return res