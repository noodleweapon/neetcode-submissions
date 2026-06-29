class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        arr = []
        for pos, rad in lights:
            arr.append((pos - rad, 1))
            arr.append((pos + rad + 1, -1))
        arr.sort()
        best, res = float("-inf"), 0
        accum = 0
        for pos, delta in arr:
            accum += delta
            if accum > best:
                best = accum
                res = pos
        return res