import math

class Solution:
    def rec(self, i, cap, stones, dp):
        if i == len(stones):
            return cap
        if dp[cap][i] != -1:
            return dp[cap][i]

        m = self.rec(i + 1, cap, stones, dp)
        if stones[i] <= cap:
            n = self.rec(i + 1, cap - stones[i], stones, dp)
            m = min(m, n)
        
        dp[cap][i] = m
        return m

    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        cap = math.ceil(s / 2)
        dp = [[-1] * (len(stones) + 1) for _ in range(cap + 1)]
        return self.rec(0, cap, stones, dp)

        # add = 0 if s % 2 == 0 else 1
        