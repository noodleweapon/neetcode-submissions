import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2)
        dp = [[-1] * (len(stones)) for _ in range(target + 2)]

        def rec(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if dp[i][total] != -1:
                return dp[i][total]
            m = min(rec(i + 1, total), rec(i + 1, total + stones[i]))
            dp[i][total] = m
            return m

        return rec(0, 0)