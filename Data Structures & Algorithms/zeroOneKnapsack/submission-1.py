class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [0] * (capacity + 1)
        for v, w in zip(profit, weight):
            for i in reversed(range(capacity + 1)):
                if i < w:
                    continue
                dp[i] = max(dp[i], dp[i - w] + v)
        
        return dp[capacity]