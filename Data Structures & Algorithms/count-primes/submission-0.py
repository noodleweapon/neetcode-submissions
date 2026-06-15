class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [True] * n
        res = 0
        for i in range(2, n):
            if not arr[i]:
                continue
            res += 1
            for j in range(i * 2, n, i):
                arr[j] = False

        return res