class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        lv = prices[0]
        hv = prices[0]
        p = 0

        for i, price in enumerate(prices):
            if price < lv:
                lv = price
                hv = price
            
            if price > hv:
                hv = price
                d = hv - lv
                if d > p:
                    p = d
        
        return p