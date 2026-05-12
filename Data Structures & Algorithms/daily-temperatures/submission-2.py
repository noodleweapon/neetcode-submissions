class Solution:
    def dailyTemperatures(self, ts: List[int]) -> List[int]:
        i = len(ts) - 1
        s = []
        out = [0] * len(ts)
        for i in reversed(range(len(ts))):
            if not s:
                s.append(i)
                continue
            if ts[s[-1]] > ts[i]:
                out[i] = s[-1] - i
                s.append(i)
                continue
            while s and ts[s[-1]] <= ts[i]:
                s.pop()
            out[i] = s[-1] - i if s else 0
            s.append(i)
        return out