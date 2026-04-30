from collections import defaultdict

class Solution:
    def isZeroDict(self, d):
        for key, val in d.items():
            if val != 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        short, long = (s1, s2) if len(s1) < len(s2) else (s2, s1)
        d = defaultdict(int)
        for c in short:
            d[c] += 1

        l = r = 0
        while r < len(long):
            d[long[r]] -= 1
            r += 1
            if r - l > len(short):
                d[long[l]] += 1
                l += 1
            if self.isZeroDict(d):
                return True
        return False