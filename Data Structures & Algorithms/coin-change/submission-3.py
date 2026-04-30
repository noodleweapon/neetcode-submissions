class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-2] * ((amount + 1))
        return self.memo(coins, amount, dp)

    def memo(self, coins: List[int], amount: int, dp) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if dp[amount] != -2:
            return dp[amount]

        m = None
        for coin in coins:
            res = self.memo(coins, amount - coin, dp)
            if res == -1:
                continue
            if not m or res < m:
                m = res

        dp[amount] = -1 if m == None else (m + 1)
        return dp[amount]

    def coinChangeLogicFail(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = 0
        coins.sort(reverse=True)
        coins.append(0)
        while amount > 0:
            for coin in coins:
                if amount < coin:
                    continue
                if coin == 0:
                    return -1
                amount -= coin
                n += 1
                break
        return n