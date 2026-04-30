class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def rec(i, buy):
            if i >= len(prices):
                return 0
            
            hold = rec(i + 1, buy)
            if buy:
                res = rec(i + 1, not buy) - prices[i]
                return max(hold, res)
            else:
                res = rec(i + 2, not buy) + prices[i]
                return max(hold, res)

        return rec(0, True)