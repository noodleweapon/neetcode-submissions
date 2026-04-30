class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def rec(i, bought_at, profit, just_sold):
            if i == len(prices):
                return profit
            if just_sold:
                return rec(i + 1, -1, profit, False)
            res = rec(i + 1, bought_at, profit, False) # just hold it
            if bought_at == -1: # buy
                res = max(res, rec(i + 1, i, profit, False))
            elif prices[i] > prices[bought_at]: # sell at profit
                P = profit + prices[i] - prices[bought_at]
                res = max(res, rec(i + 1, -1, P, True))
            return res
        
        return rec(0, -1, 0, False)
