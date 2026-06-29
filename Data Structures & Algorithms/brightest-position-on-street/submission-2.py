class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        d = defaultdict(int)
        for pos, rad in lights:
            d[pos - rad] += 1
            d[pos + rad + 1] -= 1
        best, res = float("-inf"), 0
        accum = 0
        for pos in sorted(d):
            accum += d[pos]
            if accum > best:
                best = accum
                res = pos
        return res