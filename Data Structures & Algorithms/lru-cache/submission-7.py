class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.left = Node(0, 0) # least recently used
        self.right = Node(0, 0) # most recentlly used
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity

    def remove(self, node):
        del self.d[node.key]
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
        self.d[node.key] = node
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        node = Node(key, value)
        self.insert(node)

        if len(self.d) > self.capacity:
            lru = self.left.next
            self.remove(lru)

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        
