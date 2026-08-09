class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        minPrice = prices[0]
        res = 0
        for price in prices:
            minPrice = min(minPrice, price)
            res = max(res, price - minPrice)
        return res
            