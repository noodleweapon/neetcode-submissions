from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anas = []
        for s in strs:
            ana = defaultdict(int)
            for c in s:
                ana[c] += 1
            
            found_same_ana = False
            for i, _ana in enumerate(anas):
                if ana != _ana:
                    continue
                res[i].append(s)
                found_same_ana = True
                break
            if found_same_ana:
                continue

            anas.append(ana)
            res.append([s])
        return res