class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class Level:
    def __init__(self, freq):
        self.left = Node('', -1)
        self.right = Node('', -1)
        self.left.next, self.right.prev = self.right, self.left
        self.next = None
        self.prev = None
        self.size = 0
        self.freq = freq
    
    def remove_node(self, node):
        self.size -= 1
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert_node(self, node):
        self.size += 1
        rear = self.right.prev
        rear.next = self.right.prev = node
        node.prev, node.next = rear, self.right

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Level(-1)
        self.right = Level(-1)
        self.left.next, self.right.prev = self.right, self.left

        self.levels = {}
        self.nodes = {}
        self.use = defaultdict(int)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]
        # remove from prev level
        prev_level = self.levels[self.use[key]]
        prev_level.remove_node(node)
        if prev_level.size == 0:
            level_prv, level_nxt = prev_level.prev, prev_level.next
            self.remove_level(prev_level)
        else:
            level_prv, level_nxt = prev_level, prev_level.next

        # add to new level
        self.use[key] += 1
        if self.use[key] in self.levels:
            next_level = self.levels[self.use[key]]
        else:
            next_level = Level(self.use[key])
            self.insert_level(level_prv, next_level, level_nxt)
        next_level.insert_node(node)

        return self.nodes[key].value

    def put(self, key: int, value: int) -> None:
        # evict
        if self.cap == 0 and self.use[key] == 0:
            level = self.left.next
            node = level.left.next
            level.remove_node(node)
            if level.size == 0:
                self.remove_level(level)
            self.nodes.pop(node.key, None)
            self.use.pop(node.key, None)
            self.cap += 1

        # take node from level or create new node
        if self.use[key] > 0:
            prev_level = self.levels[self.use[key]]
            node = self.nodes[key]
            node.value = value
            prev_level.remove_node(node)
            if prev_level.size == 0:
                level_prv, level_nxt = prev_level.prev, prev_level.next
                self.remove_level(prev_level)
            else:
                level_prv, level_nxt = prev_level, prev_level.next
        else:
            node = Node(key, value)
            self.nodes[key] = node
            self.cap -= 1
            level_prv, level_nxt = self.left, self.left.next

        # add node to new level
        self.use[key] += 1
        if self.use[key] in self.levels:
            next_level = self.levels[self.use[key]]
        else:
            next_level = Level(self.use[key])
            self.insert_level(level_prv, next_level, level_nxt)
        next_level.insert_node(node)

    def insert_level(self, prev_level, level, next_level):
        prev_level.next = next_level.prev = level
        level.prev, level.next = prev_level, next_level
        self.levels[level.freq] = level
        
    def remove_level(self, level):
        prv, nxt = level.prev, level.next
        prv.next, nxt.prev = nxt, prv
        self.levels.pop(level.freq, None)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)