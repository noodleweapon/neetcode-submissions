class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i1 = i2 = 0
        n1, n2 = len(s), len(t)
        while i1 < n1 and i2 < n2:
            if s[i1] == t[i2]:
                i1 += 1
                i2 += 1
            else:
                i1 += 1
        
        return n2 - i2
        



        # append to s.

        # co(aching)ding
        # coding
        # 12

        # abcde