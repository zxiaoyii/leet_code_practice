class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit_of_the_day = price - min_price
            max_profit = max(max_profit, max_profit_of_the_day)   
        return max_profit
