class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Y, X = len(grid), len(grid[0])
        seen = set()
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def rec(y, x):
            if min(x, y) < 0:
                return 0
            if x >= X or y >= Y:
                return 0
            if (y, x) in seen:
                return 0
            if grid[y][x] == 0:
                return 0
            
            seen.add((y, x))
            count = 1
            for [_y, _x] in ds:
                count += rec(y + _y, x + _x)
            return count
        
        m = 0
        for y in range(Y):
            for x in range(X):
                if (y, x) in seen:
                    continue
                if grid[y][x] == 0:
                    continue
                m = max(m, rec(y, x))
        return m
        