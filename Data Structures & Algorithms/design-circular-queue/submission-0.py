class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.l = 0 # start index (inclusive, currently occupied)
        self.r = 0 # next available for enqueue
        self.k = k

    def enQueue(self, value: int) -> bool: # ok
        if self.isFull():
            return False
        self.arr[self.r % self.k] = value
        self.r += 1
        return True

    def deQueue(self) -> bool: # ok
        if self.isEmpty():
            return False
        v = self.arr[self.l % self.k]
        self.l += 1
        return True

    def Front(self) -> int: # ok
        if self.isEmpty():
            return -1
        return self.arr[self.l % self.k]

    def Rear(self) -> int: # ok
        if self.isEmpty():
            return -1
        return self.arr[(self.r - 1) % self.k]

    def isEmpty(self) -> bool: # ok
        return self.l == self.r
        
    def isFull(self) -> bool: # ok
        return self.l + self.k == self.r # so the next write would overwrite.



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()