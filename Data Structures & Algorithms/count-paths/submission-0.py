class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def rec(y, x):
            if y == m:
                return 0
            if x == n:
                return 0
            if x == n - 1 and y == m - 1:
                return 1
            count = 0
            count += rec(y + 1, x)
            count += rec(y, x + 1)
            return count
        return rec(0, 0)
        