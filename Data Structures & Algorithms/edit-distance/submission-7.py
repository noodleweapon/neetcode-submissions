class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        memo = {}
        def rec(i1, i2):
            if i1 == n1:
                return n2 - i2
            if i2 == n2:
                return n1 - i1
            key = (i1, i2)
            if key in memo:
                return memo[key]
            cost = 0 if word1[i1] == word2[i2] else 1
            memo[key] = min(
                rec(i1 + 1, i2 + 1) + cost,
                rec(i1 + 1, i2) + 1,
                rec(i1, i2 + 1) + 1
            )
            return memo[key]
        
        return rec(0, 0)