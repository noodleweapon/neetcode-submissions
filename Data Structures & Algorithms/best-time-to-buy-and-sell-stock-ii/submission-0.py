class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        p = 0
        for i in range(1, len(prices)):
            p += max(0, prices[i] - prices[i - 1])
        return p