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
        s = sum(stones)
        cap = s // 2
        add = 0 if s % 2 == 0 else 1
        return add + self.rec(0, cap, stones)
        