class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        R = len(grid)
        C = len(grid[0])

        def flood(r, c, d):
            if grid[r][c] != 0:
                grid[r][c] = d

            for [dr, dc] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0:
                    continue
                if nr >= R or nc >= C:
                    continue
                if grid[nr][nc] <= d:
                    continue
                flood(nr, nc, d + 1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] != 0:
                    continue
                flood(r, c, 0)
        