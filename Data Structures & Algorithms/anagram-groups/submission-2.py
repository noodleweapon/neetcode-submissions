from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anas = []
        for s in strs:
            ana = defaultdict(int)
            for c in s:
                ana[c] += 1
            for i, _ana in enumerate(anas):
                if ana == _ana:
                    res[i].append(s)
                else:
                    anas.append(ana)
                    res.append([s])
        return res