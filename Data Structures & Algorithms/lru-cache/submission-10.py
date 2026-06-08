class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {} # [key]: Node
        self.left = Node('', -1)
        self.right = Node('', -1)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.remove(node)
        self.append(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.remove(node)
        else:
            node = Node(key, value)
            self.cap -= 1
        self.append(node)
        if self.cap < 0:
            self.cap += 1
            self.remove(self.left.next)
        

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
        self.dict.pop(node.key, None)

    def append(self, node):
        rear = self.right.prev
        rear.next = self.right.prev = node
        node.prev, node.next = rear, self.right
        self.dict[node.key] = node

