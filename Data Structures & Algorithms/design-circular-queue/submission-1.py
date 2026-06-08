class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # LEFT, A, rear, RIGHT
        new_rear = Node(value)
        rear = self.right.prev
        rear.next = self.right.prev = new_rear
        new_rear.prev, new_rear.next = rear, self.right
        self.cap -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        front = self.left.next
        front.next.prev, self.left.next = self.left, front.next
        self.cap += 1
        return True
        
    def Front(self) -> int:
        return self.left.next.value

    def Rear(self) -> int:
        return self.right.prev.value

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.cap == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()