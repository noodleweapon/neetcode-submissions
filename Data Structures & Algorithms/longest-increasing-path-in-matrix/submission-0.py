class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        g = [[1] * N for _ in range(N)]

        def rec(r, c):
            cell = matrix[r][c]
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    continue
                if matrix[nr][nc] >= cell:
                    continue
                g[r][c] = max(g[r][c], rec(nr, nc) + 1)
            return g[r][c]

        for r in range(N):
            for c in range(N):
                rec(r, c)

        M = 1
        for r in range(N):
            for c in range(N):
                M = max(M, g[r][c])
        return M