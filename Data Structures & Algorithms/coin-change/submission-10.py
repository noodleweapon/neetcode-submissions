class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo = {}
        def rec(i, rem, steps):
            if (i, rem) in memo:
                return memo[(i, rem)]

            if i == len(coins):
                return steps if rem == 0 else float("inf")
            
            result = float("inf")
            for k in range((rem // coins[i]) + 1):
                result = min(result, rec(i + 1, rem - k * coins[i], steps + k))
            memo[(i, rem)] = result
            return result

        M = rec(0, amount, 0)
        if M == float("inf"):
            return -1
        return M