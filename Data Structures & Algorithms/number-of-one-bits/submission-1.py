class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 0
        for i in range(32):
            if n & 1 == 1:
                k += 1
            n = n >> 1
        return k