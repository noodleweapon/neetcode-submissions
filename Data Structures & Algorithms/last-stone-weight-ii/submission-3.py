import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2)

        def rec(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            return min(rec(i + 1, total), rec(i + 1, total + stones[i]))

        return rec(0, 0)