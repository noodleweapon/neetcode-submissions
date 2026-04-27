class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if x < c:
                    continue
                steps = dp[x - c] + 1
                dp[x] = min(dp[x], steps)

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]