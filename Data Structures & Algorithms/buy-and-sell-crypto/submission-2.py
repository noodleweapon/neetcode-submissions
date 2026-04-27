class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        h = prices[-1]
        profit = 0
        for i, price in enumerate(reversed(prices)):
            h = max(h, price)
            profit = max(profit, h - price)
        return profit