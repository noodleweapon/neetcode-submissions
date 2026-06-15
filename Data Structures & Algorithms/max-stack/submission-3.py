class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.prev = None
        self.next = None


class MaxStack:

    def __init__(self):
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
        self.deleted = set()
        self.heap = []
        self.idx = 0

    def push(self, x: int) -> None:
        top = self.right.prev
        self.idx -= 1
        node = Node(x, self.idx)
        top.next = self.right.prev = node
        node.prev, node.next = top, self.right
        heapq.heappush(self.heap, (-node.val, node.idx, node))
        
    def pop(self) -> int:
        node = self.right.prev
        self.deleted.add(node)
        self.delete_node(node)
        return node.val

    def top(self) -> int: ## O(1)
        return self.right.prev.val

    def peekMax(self) -> int:
        self.lazy_heap()
        return -self.heap[0][0]

    def popMax(self) -> int:
        self.lazy_heap()
        neg_val, node_idx, node = heapq.heappop(self.heap)
        self.delete_node(node)
        return -neg_val
    
    def delete_node(self, node):
        L, R = node.prev, node.next
        L.next, R.prev = R, L

    def lazy_heap(self):
        while self.heap and self.heap[0][2] in self.deleted:
            node = self.heap[0][2]
            self.deleted.remove(node)
            heapq.heappop(self.heap)

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
