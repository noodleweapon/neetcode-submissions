class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append((val, val))
        else:
            prev_min = self.s[-1][1]
            self.s.append((val, min(val, prev_min)))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]
        
    def getMin(self) -> int:
        return self.s[-1][1]
        