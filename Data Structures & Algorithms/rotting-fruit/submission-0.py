class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Y, X = len(grid), len(grid[0])
        seen = set()
        queue = deque([])

        for y in range(Y):
            for x in range(X):
                if grid[y][x] != 2:
                    continue
                queue.append((y, x))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        length = -1
        while queue:
            length += 1
            for i in range(len(queue)):
                cy, cx = queue.popleft()
                for dy, dx in directions:
                    y = cy + dy
                    x = cx + dx
                    if min(x, y) < 0:
                        continue
                    if x >= X or y >= Y:
                        continue
                    if (y, x) in seen:
                        continue
                    if grid[y][x] != 1:
                        continue
                    queue.append((y, x))
                    seen.add((y, x))

        for y in range(Y):
            for x in range(X):
                if grid[y][x] != 1:
                    continue
                if (y, x) in seen:
                    continue
                return -1

        return length
                


