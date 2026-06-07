class FreqStack:

    def __init__(self):
        self.stacks = []
        self.freqs = {}

    def push(self, val: int) -> None:
        freq = self.freqs.get(val, 0)
        while len(self.stacks) <= freq:
            self.stacks.append([])
        self.stacks[freq].append(val)
        self.freqs[val] = freq + 1

    def pop(self) -> int:
        maxf = len(self.stacks)
        res = self.stacks[maxf - 1].pop()
        if not self.stacks[maxf - 1]:
            self.stacks.pop()
        self.freqs[res] -= 1
        return res
        

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()