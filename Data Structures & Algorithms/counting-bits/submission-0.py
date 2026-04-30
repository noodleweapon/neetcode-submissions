class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for k in range(n):
            t = 0
            while k:
                if k & 1:
                    t += 1
                k = k >> 1
            res.append(t)
        return res