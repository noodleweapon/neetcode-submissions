class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            if n & 1 == 1:
                bit = 1 << (31 - i)
                out = out | bit
            n = n >> 1
        return out