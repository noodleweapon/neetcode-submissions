class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):
            if curr == None:
                break
            curr = curr.next
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            return

        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(val)
        

    def remove(self, index: int) -> bool:
        curr = self.head
        for i in range(index - 1):
            if curr == None:
                return False
            curr = curr.next
        
        if curr.next == None:
            return False

        if curr.next.next == None:
            return False

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        curr = self.head
        nums = []
        while curr != None:
            nums.append(curr)
            curr = curr.next
        return nums
