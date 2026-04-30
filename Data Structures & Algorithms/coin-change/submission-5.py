class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        M = float("inf")
        def rec(i, rem, steps):
            nonlocal M
            if i == len(coins):
                if rem == 0:
                    M = min(M, steps)
                return
            
            for k in range((rem // coins[i]) + 1):
                rec(i + 1, rem - k * coins[i], steps + k)

        rec(0, amount, 0)
        if M == float("inf"):
            return -1
        return M