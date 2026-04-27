class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            v = 0
            while n > 0:
                k = n % 10
                v += k * k
                n = int(n / 10)
            n = v
        return 1 in seen
