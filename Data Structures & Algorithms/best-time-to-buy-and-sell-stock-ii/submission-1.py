class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(1, len(prices)):
            p += max(0, prices[i] - prices[i - 1])
        return p