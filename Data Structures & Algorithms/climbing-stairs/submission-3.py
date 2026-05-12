class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a = 0
        b = 1
        for i in range(n):
            c = a + b
            a = b
            b = c

        return b