class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        Y, X = len(grid), len(grid[0])
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        s = set()
        for y in range(Y):
            for x in range(X):
                if grid[y][x] != 0:
                    continue
                q.append((y, x))
                s.add((y, x))
        
        length = 1
        while q:
            for i in range(len(q)):
                cy, cx = q.popleft()
                for dy, dx in ds:
                    _y = cy + dy
                    _x = cx + dx
                    if min(_y, _x) < 0:
                        continue
                    if _y >= Y or _x >= X:
                        continue
                    if grid[_y][_x] == -1:
                        continue
                    if (_y, _x) in s:
                        continue
                    grid[_y][_x] = length
                    q.append((_y, _x))
                    s.add((_y, _x))
            
            length += 1



        # def rec(y, x):
        #     if grid[y][x] == 0:
        #         return 0
        #     options = []
        #     for dy, dx in ds:
        #         _y = y + dy
        #         _x = x + dx
        #         if min(_y, _x) < 0:
        #             continue
        #         if _y >= Y or _x >= X:
        #             continue
        #         cell = grid[_y][_x]
        #         if cell == -1:
        #             continue
        #         if cell == INF:
        #             options.append(rec(_y, _x))
        #         else:
        #             options.append(cell)
        #     grid[y][x] = 1 + min(options)
        #     return grid[y][x]
        
        # for y in range(Y):
        #     for x in range(X):
        #         if grid[y][x] != INF:
        #             continue
        #         rec(y, x)

