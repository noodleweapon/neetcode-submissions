class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque([])
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))

        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)]:
                    if nr < 0 or nc < 0 or nr >= R or nc >= C:
                        continue
                    if grid[nr][nc] == -1:
                        continue
                    if grid[nr][nc] <= d:
                        continue
                    grid[nr][nc] = d
                    q.append((nr, nc))

        