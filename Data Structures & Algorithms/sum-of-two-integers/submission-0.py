class Solution:
    def getSum(self, a: int, b: int) -> int:
        total = 0
        C = 0
        bits = max(a.bit_length(), b.bit_length())
        for i in range(bits):
            bit = 1 << i
            A = a & bit
            B = b & bit

            res = ((A ^ B) ^ C) << i
            total = total | res
            C = (A | B) & C

        return total