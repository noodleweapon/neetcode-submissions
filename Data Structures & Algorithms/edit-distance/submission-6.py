class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        @cache
        def rec(i1, i2):
            if i1 == n1:
                return n2 - i2
            if i2 == n2:
                return n1 - i1
                
            cost = 0 if word1[i1] == word2[i2] else 1
            return min(
                rec(i1 + 1, i2 + 1) + cost,
                rec(i1 + 1, i2) + 1,
                rec(i1, i2 + 1) + 1
            )
        
        return rec(0, 0)