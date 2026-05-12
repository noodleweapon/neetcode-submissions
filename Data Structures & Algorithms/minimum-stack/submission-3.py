class MinStack:

    def __init__(self):
        self.stack = []
        self.min_so_far = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min_so_far = val
        if self.min_so_far:
            new_min_so_far = min(new_min_so_far, self.min_so_far[-1])
        self.min_so_far.append(new_min_so_far)

    def pop(self) -> None:
        self.stack.pop()
        self.min_so_far.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_so_far[-1]

        
