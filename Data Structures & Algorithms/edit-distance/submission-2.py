class Solution:
    def minDistance(self, a: str, b: str) -> int:
        x = max(len(a), len(b))
        y = self.rec(a, b, 0, 0)
        print(x, y)
        return x - y
    
    def rec(self, a, b, i, j):
        A = len(a)
        B = len(b)

        if i == len(a):
            return i - j + 2
        if j == len(b):
            return j - i + 2

        if a[i] == b[j]:
            return 1 + self.rec(a, b, i + 1, j + 1)
        
        return min(self.rec(a, b, i + 1, j), self.rec(a, b, i, j + 1))
