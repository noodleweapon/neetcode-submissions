class MyQueue:

    def __init__(self):
        self.grow = []
        self.shrink = []

    def push(self, x: int) -> None:
        self.grow.append(x)

    def pop(self) -> int:
        self.transfer()
        return self.shrink.pop()

    def peek(self) -> int:
        self.transfer()
        return self.shrink[-1]
    
    def transfer(self):
        while self.grow:
            top = self.grow.pop()
            self.shrink.append(top)
        
    def empty(self) -> bool:
        if self.grow:
            return False
        if self.shrink:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()