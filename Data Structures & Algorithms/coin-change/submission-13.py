class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float("inf")] * (amount + 1)
        memo[0] = 0
        for i, c in enumerate(coins):
            for v in range(1, 1 + amount):
                if v >= c:
                    memo[v] = min(memo[v], memo[v - c] + 1)

        if memo[amount] == float("inf"):
            return -1
        return memo[amount]