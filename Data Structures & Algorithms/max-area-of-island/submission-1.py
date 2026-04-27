class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        X = len(grid[0])
        Y = len(grid)
        seen = set()

        def rec(x, y):
            if x < 0 or y < 0:
                return 0
            if x >= X or y >= Y:
                return 0
            if grid[y][x] == 0:
                return 0
            coord = (x, y)
            if coord in seen:
                return 0
            seen.add(coord)
            return (
                rec(x - 1, y) +
                rec(x + 1, y) +
                rec(x, y - 1) +
                rec(x, y + 1) + 1
            )
        
        M = 0
        for y in range(Y):
            for x in range(X):
                m = rec(x, y)
                M = max(m, M)
        
        return M