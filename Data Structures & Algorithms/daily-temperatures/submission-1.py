class Solution:
    def dailyTemperatures(self, ts: List[int]) -> List[int]:
        res = [0] * len(ts)
        s = []

        for i in reversed(range(len(ts))):
            t = ts[i]
            while s and s[-1][0] <= t:
                s.pop()
            
            if s:
                res[i] = s[-1][1] - i
            
            s.append((t, i))

        return res