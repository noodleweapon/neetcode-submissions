class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * (n + 1) for _ in range(m)]

        def rec(y, x):
            if y == m:
                return 0
            if x == n:
                return 0
            if dp[y][x] != -1:
                return dp[y][x]
            if x == n - 1 and y == m - 1:
                return 1
            count = 0
            count += rec(y + 1, x)
            count += rec(y, x + 1)
            dp[y][x] = count
            return count
        return rec(0, 0)
        