class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 + n2 != len(s3):
            return False
        
        memo = {}
        def rec(i1, i2):
            key = (i1, i2)
            if i1 == n1 and i2 == n2:
                return True
            if i1 > n1 or i2 > n2:
                return False
            if key in memo:
                return memo[key]
            i3 = i1 + i2
            if i1 < n1 and s3[i3] == s1[i1] and rec(i1 + 1, i2):
                memo[key] = True
                return True
            if i2 < n2 and s3[i3] == s2[i2] and rec(i1, i2 + 1):
                memo[key] = True
                return True
            memo[key] = False
            return False
        
        return rec(0, 0)