class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        Y, X = len(grid), len(grid[0])
        directions = []
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                directions.append((y, x))

        start = grid[0][0]
        if start == 1:
            return -1

        queue = deque([(0, 0)])
        seen = set((0, 0))
        length = 0

        while queue:
            length += 1
            for i in range(len(queue)):
                yc, xc = queue.popleft()
                print(yc, xc)
                if yc == Y - 1 and xc == X - 1:
                    return length
                for dy, dx in directions:
                    y = yc + dy
                    x = xc + dx
                    if min(y, x) < 0:
                        continue
                    if y >= Y or x >= X:
                        continue
                    if (y, x) in seen:
                        continue
                    if grid[y][x] != 0:
                        continue
                    queue.append((y, x))
                    seen.add((y, x))
        return -1
            
                    