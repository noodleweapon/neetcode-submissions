class Solution:
    def numDistinct(self, s1: str, s2: str) -> int:
        k = len(s1) - len(s2)
        if k < 0:
            return 0
        memo = {}
        def rec(i1, i2):
            if i1 == len(s1):
                return 1 if i2 == len(s2) else 0
            key = (i1, i2)
            if key in memo:
                return memo[key]
            z = rec(i1 + 1, i2)
            if i1 < len(s1) and i2 < len(s2) and s1[i1] == s2[i2]:
                z += rec(i1 + 1, i2 + 1)
            memo[key] = z
            return z

        return rec(0, 0)