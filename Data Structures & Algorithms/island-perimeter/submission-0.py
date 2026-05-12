class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set()
        s = 0
        def rec(r, c):
            visited.add((r, c))
            N = r == 0 or grid[r - 1][c] == 0
            S = r == R - 1 or grid[r + 1][c] == 0
            W = c == 0 or grid[r][c - 1] == 0
            E = c == C - 1 or grid[r][c + 1] == 0

            tot = N + S + W + E

            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue
                if grid[nr][nc] == 0:
                    continue
                if (nr, nc) in visited:
                    continue
                tot += rec(nr, nc)
            return tot
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                return rec(r, c)