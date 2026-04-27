class Solution:
    def minDistance(self, a: str, b: str) -> int:
        return self.rec(a, b, 0, 0)
    
    def rec(self, a, b, i, j):
        A = len(a)
        B = len(b)

        if i == A:
            return abs(B - j)
        if j == B:
            return abs(A - i)

        if a[i] == b[j]:
            return self.rec(a, b, i + 1, j + 1)
        
        return min(1 + self.rec(a, b, i + 1, j),
            1 + self.rec(a, b, i, j + 1),
            1 + self.rec(a, b, i + 1, j + 1))
