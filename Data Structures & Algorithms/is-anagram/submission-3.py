from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ss = defaultdict(int)
        tt = defaultdict(int)
        for c in s:
            ss[c] += 1
        for c in t:
            tt[c] += 1
        
        return ss == tt