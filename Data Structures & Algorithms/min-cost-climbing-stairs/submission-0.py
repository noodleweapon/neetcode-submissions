class Solution:
    def rec(self, cost, ind):
        if ind < 2:
            return 0
        a = self.rec(cost, ind - 1) + cost[ind - 1]
        b = self.rec(cost, ind - 2) + cost[ind - 2]
        return min(a, b)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.rec(cost, len(cost))