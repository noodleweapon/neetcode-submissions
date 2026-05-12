from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)
        for _s in s:
            sd[_s] += 1
        for _t in t:
            td[_t] += 1
        return sd == td