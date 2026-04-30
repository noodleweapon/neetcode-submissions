import math

class Solution:
    def rec(self, i, cap, stones):
        if i == len(stones):
            return cap
        
        m = self.rec(i + 1, cap, stones)
        if stones[i] <= cap:
            n = self.rec(i + 1, cap - stones[i], stones)
            m = min(m, n)
        return m

    def lastStoneWeightII(self, stones: List[int]) -> int:
        cap = sum(stones) // 2
        return self.rec(0, cap, stones)
        