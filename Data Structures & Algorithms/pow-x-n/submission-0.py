class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg_pow = n < 0
        n = abs(n)
        o = 1
        for i in range(n):
            o *= x
        return 1 / o if neg_pow else o