class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        items = self.m[key]
        l = 0
        r = len(items) - 1
        while l <= r:
            m = (l + r) // 2
            t, v = items[m]
            if l == r:
                if t >= timestamp:
                    return v
                else:
                    return ""
            if timestamp == t:
                return v
            elif t > timestamp:
                r = m
            else:
                l = m + 1
        return ""