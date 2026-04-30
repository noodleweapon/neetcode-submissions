class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        m = None
        for coin in coins:
            res = self.coinChange(coins, amount - coin)
            if res == -1:
                continue
            cc = 1 + res
            if not m or cc < m:
                m = cc

        if m == None:
            return -1
        return m

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