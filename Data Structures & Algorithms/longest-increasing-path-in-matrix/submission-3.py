class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        g = [[1] * C for _ in range(R)]
        seen = [[False] * C for _ in range(R)]

        def rec(r, c):
            if seen[r][c]:
                return g[r][c]
            cell = matrix[r][c]
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue
                if matrix[nr][nc] >= cell:
                    continue
                g[r][c] = max(g[r][c], rec(nr, nc) + 1)
            seen[r][c] = True
            return g[r][c]

        M = 1
        for r in range(R):
            for c in range(C):
                M = max(M, rec(r, c))
        return M