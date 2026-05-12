class Solution:
    def rec(self, y, x, grid):
        if min(x, y) < 0:
            return
        X, Y = len(grid[0]), len(grid)
        if x >= X or y >= Y:
            return
        if grid[y][x] == "0":
            return
        grid[y][x] = "0"
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for (_y, _x) in dirs:
            self.rec(y + _y, x + _x, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        X, Y = len(grid[0]), len(grid)
        islands = 0

        for y in range(Y):
            for x in range(X):
                if grid[y][x] == "0":
                    continue
                self.rec(y, x, grid)
                islands += 1
        
        return islands
        


        # total = 0
        # connected = 0
        # for y, row in enumerate(grid):
        #     for x, cell in enumerate(row):
        #         if cell == "0":
        #             continue
        #         total += 1
        #         isConn = False
        #         if x > 0 and row[x - 1] == "1":
        #             isConn = True
        #         if y > 0 and grid[y - 1][x] == "1":
        #             isConn = True
        #         if isConn:
        #             connected += 1
        # return total - connected


