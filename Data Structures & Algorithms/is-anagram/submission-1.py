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
            tt[t] += 1
        
        for a, b in [[ss, tt], [tt, ss]]:
            for k, v in a.items():
                if k not in b:
                    return False
                vv = tt[k]
                if vv != v:
                    return False
        return True