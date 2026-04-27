class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[None] * (n2 + 1) for _ in range(n1 + 1)]

        for i1 in range(n1 + 1):
            dp[i1][n2] = n1 - i1

        for i2 in range(n2 + 1):
            dp[n1][i2] = n2 - i2
        
        for i1 in reversed(range(n1)):
            for i2 in reversed(range(n2)):
                diag_cost = 0 if word1[i1] == word2[i2] else 1
                m = min(
                    diag_cost + dp[i1 + 1][i2 + 1],
                    1 + dp[i1 + 1][i2],
                    1 + dp[i1][i2 + 1]
                )
                dp[i1][i2] = m

        return dp[0][0]