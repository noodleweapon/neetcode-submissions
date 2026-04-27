class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg_pow = n < 0
        n = abs(n)

        o = 1
        while n > 0:
            if n % 2 == 1:
                o *= x
            x = x * x
            n = n // 2

        return 1 / o if neg_pow else o