class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s1, s2 = (s, t) if len(s) < len(t) else (t, s)
        n1, n2 = len(s1), len(s2) # <
        if n1 == n2:
            diff = 0
            for i in range(n1):
                c1, c2 = s1[i], s2[i]
                if c1 != c2:
                    diff += 1
                    if diff == 2:
                        return False
            return diff == 1
        
        if n2 - n1 != 1:
            return False

        i1 = i2 = 0
        while i1 < n1 and i2 < n2:
            c1, c2 = s1[i1], s2[i2]
            if c1 == c2:
                i1 += 1
                i2 += 1
            else:
                i2 += 1
        return i1 == n1

        # ab
        # acb
            
