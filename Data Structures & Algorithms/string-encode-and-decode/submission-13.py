class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        res += str(len(strs)) + ','
        for s in strs:
            res += str(len(s)) + ','
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        split = s.split(',')
        n = int(split[0])
        ls = split[1:n+1]
        offset = len(','.join(split[:n+1])) + 1
        res = []
        for l in ls:
            res.append(s[offset:offset+int(l)])
            offset += int(l)
        return res