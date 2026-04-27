class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        X = len(grid[0])
        Y = len(grid)
        seen = set()

        def rec(x, y):
            if x < 0 or y < 0:
                return
            if x >= X or y >= Y:
                return
            if grid[y][x] == '0':
                return
            coord = (x, y)
            if coord in seen:
                return
            seen.add(coord)
            rec(x - 1, y)
            rec(x + 1, y)
            rec(x, y - 1)
            rec(x, y + 1)
        
        cc = 0
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == '0':
                    continue
                coord = (x, y)
                if coord in seen:
                    continue
                cc += 1
                rec(x, y)
        
        return cc