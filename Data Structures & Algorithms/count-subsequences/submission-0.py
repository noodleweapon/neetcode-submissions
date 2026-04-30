class Solution:
    def numDistinct(self, s1: str, s2: str) -> int:
        k = len(s1) - len(s2)
        if k < 0:
            return 0
        
        n = 0
        def rec(i1, i2):
            nonlocal n
            if i1 == len(s1):
                if i2 == len(s2):
                    n += 1
                return
            
            rec(i1 + 1, i2)
            if i1 < len(s1) and i2 < len(s2) and s1[i1] == s2[i2]:
                rec(i1 + 1, i2 + 1)

        rec(0, 0)
        return n