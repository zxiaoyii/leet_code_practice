class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = cur_price - min_value_before_it
        # max_profit = max(max_profit, profit)

        dp = [0] * len(prices)
        profit = 0
        max_profit = 0
        min_value = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            profit = price - min_value
            max_profit = max(max_profit, profit)
            min_value = min(min_value, price)

        return max_profit            