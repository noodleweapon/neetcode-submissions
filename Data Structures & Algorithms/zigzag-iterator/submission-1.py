class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vs = [v1, v2]
        self.n = len(self.vs)
        self.i = 0
        self.j = 0
        self.ended = True
        for j in range(self.n):
            if len(self.vs[j]) > 0:
                self.j = j
                self.ended = False
                break

    def next(self) -> int:
        if self.ended:
            return float("-inf")
        res = self.vs[self.j][self.i]
        prev_j = self.j
        for j in range(self.j + 1, self.n):
            if self.i < len(self.vs[j]):
                self.j = j
                break
        if self.j == prev_j:
            self.i += 1
            for j in range(self.n):
                if self.i < len(self.vs[j]):
                    self.j = j
                    break

        self.ended = self.i >= len(self.vs[self.j])
        return res
        
    def hasNext(self) -> bool:
        return not self.ended

        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
