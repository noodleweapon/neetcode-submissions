import math

class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        items = self.m[key]
        l = 0
        r = len(items) - 1
        if items[-1][0] <= timestamp:
            return items[-1][1]
        while l < r:
            m = math.ceil((l + r) / 2)
            t, v = items[m]
            if timestamp == t:
                return v
            elif t > timestamp:
                r = m - 1
            else:
                l = m
        return ""