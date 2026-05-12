class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0] = costs[0].copy()
        print(dp)
        for i in range(1, n):
            (pA, pB, pC) = dp[i - 1]
            (a, b, c) = costs[i]
            A = a + min(pB, pC)
            B = b + min(pA, pC)
            C = c + min(pA, pB)
            dp[i] = [A, B, C]
        
        return min(dp[n - 1])