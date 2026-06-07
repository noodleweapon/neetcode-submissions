class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.kv[key]
        if not arr:
            return ""
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r + 1) // 2
            cond = arr[m][1] <= timestamp
            if cond:
                l = m
            else:
                r = m - 1
        if arr[l][1] <= timestamp:
            return arr[l][0]
        return ""
