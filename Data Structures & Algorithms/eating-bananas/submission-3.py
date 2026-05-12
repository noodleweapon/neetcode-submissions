import math

class Solution:
    def success(self, piles, h, k):
        t = 0
        for pile in piles:
            t += math.ceil(pile / k)
            if t > h:
                return False
        return True

    def bst(self, piles, h, lk, hk):
        if lk > hk: return None
        mk = lk + ((hk - lk) // 2)
        mv = self.success(piles, h, mk)
        if lk == hk:
            return mk if mv else None
        if mv:
            prev = self.bst(piles, h, lk, mk - 1)
            if prev == None:
                return mk
            else:
                return prev
        else:
            return self.bst(piles, h, mk + 1, hk)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lk = 1
        hk = max(piles)
        return self.bst(piles, h, lk, hk)

