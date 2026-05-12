class Solution:
    def reverseBits(self, n: int) -> int:
        t = 0
        for i in range(32):
            bit = n & 1
            n = n >> 1
            t = t << 1
            t = t ^ bit
        return t
