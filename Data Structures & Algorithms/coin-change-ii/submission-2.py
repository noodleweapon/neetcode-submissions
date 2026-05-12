class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        # coins.sort(reverse=True)
        for coin in coins:
            for i in range(1, amount + 1):
                if i < coin:
                    continue
                dp[i] += dp[i - coin]
        return dp[amount]