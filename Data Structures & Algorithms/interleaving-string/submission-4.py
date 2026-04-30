class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        def rec(i1, i2):
            if i1 == n1 and i2 == n2:
                return True
            if i1 > n1 or n2 > n2:
                return False

            i3 = i1 + i2
            if s3[i3] == s1[i1] and rec(i1 + 1, i2):
                return True
            if s3[i3] == s2[i2] and rec(i1, i2 + 1):
                return True
            return False
        
        return rec(0, 0)