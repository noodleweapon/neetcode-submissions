class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0
        for i in range(1, len(cost)):
            c = min(a + cost[i - 1], b + cost[i])
            a = b
            b = c
        return b