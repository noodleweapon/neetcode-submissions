class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def rec(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            hold = rec(i + 1, buy)
            if buy:
                res = rec(i + 1, not buy) - prices[i]
                res = max(hold, res)
            else:
                res = rec(i + 2, not buy) + prices[i]
                res = max(hold, res)
            memo[(i, buy)] = res
            return res
        return rec(0, True)