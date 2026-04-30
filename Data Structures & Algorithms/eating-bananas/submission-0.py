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
        mk = lk + ((hk - lk) // 2)
        if lk == hk:
            return mk
        mv = self.success(piles, h, mk)
        if mv:
            return self.bst(piles, h, lk, mk)
        else:
            return self.bst(piles, h, mk, hk)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lk = min(piles)
        hk = max(piles)
        return self.bst(piles, h, lk, hk)