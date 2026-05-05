class FreqStack:

    def __init__(self):
        self.f = defaultdict(int)
        self.stacks = [[]]

    def push(self, val: int) -> None:
        self.f[val] += 1
        f = self.f[val]
        if len(self.stacks) == f:
            self.stacks.append([])
        self.stacks[f].append(val)

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        f = self.f[val]
        self.f[val] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()