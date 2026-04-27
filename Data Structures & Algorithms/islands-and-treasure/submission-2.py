class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        R = len(grid)
        C = len(grid[0])

        Q = deque([])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    Q.append((r, c))
        d = 0
        while Q:
            L = len(Q)
            d += 1
            for i in range(L):
                (r, c) = Q.popleft()
                for [dr, dc] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0:
                        continue
                    if nr >= R or nc >= C:
                        continue
                    if grid[nr][nc] <= d:
                        continue
                    grid[nr][nc] = d
                    Q.append((nr, nc))