class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = defaultdict(int)
        trusts = [False] * n
        for a, b in trust:
            if a == b:
                continue
            trusts[a - 1] = True
            c[b] += 1
        
        for i, t in enumerate(trusts):
            if t:
                continue
            if c[i + 1] == n - 1:
                return i + 1
        
        return -1