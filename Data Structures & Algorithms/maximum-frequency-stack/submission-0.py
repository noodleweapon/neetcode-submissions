class FreqStack:

    def __init__(self):
        self.h = []
        self.t = 0
        self.f = defaultdict(int)

    def push(self, val: int) -> None:
        self.t += 1
        self.f[val] += 1
        heapq.heappush(self.h, (-self.f[val], -self.t, val))

    def pop(self) -> int:
        (_, _, val) = heapq.heappop(self.h)
        self.f[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()