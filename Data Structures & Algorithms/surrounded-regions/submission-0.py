class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        Y, X = len(grid), len(grid[0])
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def rec(cy, cx, visited):
            visited.add((cy, cx))
            if cy == 0 or cx == 0 or cy == Y - 1 or cx == X - 1:
                grid[cy][cx] = "G"
                return

            for dy, dx in ds:
                _y = cy + dy
                _x = cx + dx
                if min(_y, _x) < 0:
                    continue
                if _y >= Y or _x >= X:
                    continue
                if grid[_y][_x] == "X":
                    continue
                if (_y, _x) in visited:
                    continue
                rec(_y, _x, visited)
            
            for dy, dx in ds:
                _y = cy + dy
                _x = cx + dx
                if grid[_y][_x] == "G":
                    grid[cy][cx] = "G"
                    return

        for y in range(Y):
            for x in range(X):
                if grid[y][x] != "O":
                    continue
                rec(y, x, set())
        
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == "O":
                    grid[y][x] = "X"
                elif grid[y][x] == "G":
                    grid[y][x] = "O"
