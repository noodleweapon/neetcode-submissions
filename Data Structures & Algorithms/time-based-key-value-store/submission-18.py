from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.d[key]) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            ts, val = self.d[key][m]
            if ts > timestamp:
                r = m - 1
            elif ts <= timestamp:
                res = val
                l = m + 1
        return res
