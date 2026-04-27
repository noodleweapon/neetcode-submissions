class Solution:
    def rec(self, y, x, grid, visited):
        if min(x, y) < 0:
            return
        X, Y = len(grid[0]), len(grid)
        if x >= X or y >= Y:
            return
        if grid[y][x] == "0":
            return
        if (y, x) in visited:
            return

        visited.add((y, x))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for (_y, _x) in dirs:
            self.rec(y + _y, x + _x, grid, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        X, Y = len(grid[0]), len(grid)
        visited = set()
        islands = 0

        for y in range(Y):
            for x in range(X):
                if grid[y][x] == "0" or (y, x) in visited:
                    continue
                self.rec(y, x, grid, visited)
                islands += 1
        
        return islands