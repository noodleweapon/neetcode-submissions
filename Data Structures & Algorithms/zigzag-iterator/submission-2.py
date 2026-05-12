class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vs = [v1, v2]
        self.q = deque()
        for i, v in enumerate(self.vs):
            if v:
                self.q.append((i, 0, len(v)))

    def next(self) -> int:
        (q_ind, cur_ind, q_n) = self.q.popleft()
        res = self.vs[q_ind][cur_ind]
        if cur_ind + 1 < q_n:
            self.q.append((q_ind, cur_ind + 1, q_n))
        return res

    def hasNext(self) -> bool:
        return len(self.q) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
