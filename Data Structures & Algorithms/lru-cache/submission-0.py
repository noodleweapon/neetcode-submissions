class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.q = deque([])

    def get(self, key: int) -> int:
        if key in self.d:
            return self.d[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            self.q.append(key)
        self.d[key] = value

        if len(self.q) > self.cap:
            top = self.q.popleft()
            self.d.pop(top)
        
