import math

class Solution:
    def canEat(self, piles, speed, h):
        hours = h
        for pile in piles:
            hours -= math.ceil(pile / speed)
            if hours < 0:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        speed = max(piles)

        while l <= r:
            m = (l + r) // 2
            if self.canEat(piles, m, h):
                speed = min(speed, m)
                r = m - 1
            else:
                l = m + 1
        return speed