class HitCounter:
    def __init__(self):
        self.f = 0
        self.d = defaultdict(int)
        self.q = deque([])

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.d:
            self.d[timestamp] = 0
            self.q.append(timestamp)
        self.d[timestamp] += 1
        self.f += 1

    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0] <= timestamp - 300:
            ts = self.q.popleft()
            self.f -= self.d[ts]
            del self.d[ts]
        return self.f

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
