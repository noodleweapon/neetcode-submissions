class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue
                dfs(nr, nc)

        for r in range(R):
            for c in [0, C - 1]:
                dfs(r, c)

        for c in range(C):
            for r in [0, R - 1]:
                dfs(r, c)

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res += 1
        return res

