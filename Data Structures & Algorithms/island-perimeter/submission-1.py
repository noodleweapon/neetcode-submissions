class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        s = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                N = r == 0 or grid[r - 1][c] == 0
                S = r == R - 1 or grid[r + 1][c] == 0
                W = c == 0 or grid[r][c - 1] == 0
                E = c == C - 1 or grid[r][c + 1] == 0
                s += N + S + W + E
        return s