class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for t in strs:
            d2 = [0] * 26
            for c in t:
                d2[ord(c) - ord('a')] += 1
            d[','.join(list(map(str, d2)))].append(t)
        return list(d.values())