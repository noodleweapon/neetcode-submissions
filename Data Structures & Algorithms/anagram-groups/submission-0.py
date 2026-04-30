from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        out = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for l in s:
                ind = alphabet.index(l)
                arr[ind] += 1
        
            out[tuple(arr)].append(s)
        
        return out.values()