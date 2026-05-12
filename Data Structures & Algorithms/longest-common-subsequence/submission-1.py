class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        # return self.rec(text1, text2, 0, 0)
        A = len(a)
        B = len(b)
        dp = [[0] * (B + 1) for _ in range(A + 1)]

        for i in range(A):
            for j in range(B):
                if a[i] == b[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[A][B]



    def rec(self, s1, s2, i1, i2):
        if i1 == len(s1) or i2 == len(s2):
            return 0
        if s1[i1] == s2[i2]:
            return 1 + self.rec(s1, s2, i1 + 1, i2 + 1)
        else:
            return max(self.rec(s1, s2, i1 + 1, i2), self.rec(s1, s2, i1, i2 + 1))
