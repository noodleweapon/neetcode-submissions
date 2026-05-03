class Solution:
    def mySqrt(self, x: int) -> int:
        def cond(m):
            return m * m <= x
        
        l, r = 0, x
        while l < r:
            m = (l + r + 1) // 2
            if cond(m):
                l = m
            else:
                r = m - 1
        return l

