class Solution:
    def numDistinct(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        if n2 > n1:
            return 0

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i1 in range(n1 + 1):
            dp[i1][n2] = 1

        for i1 in reversed(range(n1)):
            for i2 in reversed(range(n2)):
                dp[i1][i2] = dp[i1 + 1][i2]
                if s1[i1] == s2[i2]:
                    dp[i1][i2] += dp[i1 + 1][i2 + 1]


        return dp[0][0]