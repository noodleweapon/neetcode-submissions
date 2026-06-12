class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque([])
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
                    grid[r][c] = -1
                
        if len(rotten) == 0 and fresh == 0:
            return 0

        iters = -1
        while rotten:
            iters += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
                    if nr < 0 or nc < 0 or nr >= R or nc >= C:
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = -1
                    rotten.append((nr, nc))
                    fresh -= 1

        return -1 if fresh > 0 else iters

        # [1,1,0]
        # [0,1,1]
        # [0,1,2]