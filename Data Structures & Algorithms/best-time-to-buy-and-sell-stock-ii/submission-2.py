class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for price in prices[1:]:
            low = min(low, price)
            if price > low:
                profit += price - low
                low = price
        return profit