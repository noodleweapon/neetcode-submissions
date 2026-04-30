class Solution:
    def getSum(self, a: int, b: int) -> int:
        total = 0
        C = 0
        bits = max(a.bit_length(), b.bit_length())
        for i in range(bits):
            A = (a >> i) & 1
            B = (b >> i) & 1

            res = ((A ^ B) ^ C) << i
            total = total | res
            C = (A & B) | (C & (A ^ B))

        if C:
            total |= C << bits
        return total