class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.tail = Node(None, None)
        curr = self.tail
        for i in range(capacity - 1):
            node = Node(None, None)
            node.prev = curr
            curr.next = node
            curr = curr.next
        self.head = curr

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d.get(key)
            self.set_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.set_head(node)
            node.val = value
        else:
            # add to head
            new_node = Node(key, value)
            new_node.prev = self.head
            new_node.next = None
            self.head.next = new_node
            self.head = new_node
            self.d[key] = new_node

            # remove tail
            if len(self.d) > 0 and self.tail.key is not None:
                self.d.pop(self.tail.key)
                next_tail = self.tail.next
                if next_tail:
                    next_tail.prev = None
                self.tail = next_tail
            # # add to head
            # new_node = Node(key, value)
            # new_node.prev = self.head
            # self.head.next = new_node
            # self.head = new_node
            # self.d[key] = new_node

            # # remove tail
            # if self.tail.key != None:
            #     self.d.pop(self.tail.key)
            # next_tail = self.tail.next
            # if next_tail:
            #     next_tail.prev = None
            #     self.tail = next_tail
    
    def set_head(self, node):
        if node == self.head:
            return

        next_node = node.next
        prev_node = node.prev

        if next_node:
            next_node.prev = prev_node
        if prev_node:
            prev_node.next = next_node

        node.prev = self.head
        self.head = node
        node.next = None
