import copy

class Solution:
    def rec(self, i, n, k, cur, res):
        if len(cur) == k:
            res.append(copy.deepcopy(cur))
            return
        
        for j in range(i, n + 1):
            cur.append(j)
            self.rec(j + 1, n, k, cur, res)
            cur.pop()


    def combine(self, n: int, k: int) -> List[List[int]]:
        res, cur = [], []
        self.rec(1, n, k, cur, res)
        return res