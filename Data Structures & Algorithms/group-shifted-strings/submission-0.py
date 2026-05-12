class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strings:
            o = ord(s[0])
            inds = []
            for c in s:
                num = (26 + ord(c) - o) % 26
                inds.append(num)
            d[tuple(inds)].append(s)
        return list(d.values())