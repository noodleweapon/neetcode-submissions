from collections import defaultdict

class Solution:
    def isZeroDict(self, d):
        for key, val in d.items():
            if val != 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = defaultdict(int)
        for c in s1:
            d[c] -= 1

        l = r = 0
        while r < len(s2):
            d[s2[r]] += 1
            r += 1
            if r - l > len(s1):
                d[s2[l]] -= 1
                l += 1
            if self.isZeroDict(d):
                return True
        return False