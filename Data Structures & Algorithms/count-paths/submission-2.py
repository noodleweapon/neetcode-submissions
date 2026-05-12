class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [1] * m
        for r in range(1, n):
            for c in range(1, m):
                grid[c] = grid[c - 1] + grid[c]
        return grid[m - 1]