class Solution:
    def rec(self, cost, ind, dp):
        if ind < 2:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        a = self.rec(cost, ind - 1, dp) + cost[ind - 1]
        b = self.rec(cost, ind - 2, dp) + cost[ind - 2]
        dp[ind] = min(a, b)
        return dp[ind]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost) + [-1]
        return self.rec(cost, len(cost), dp)