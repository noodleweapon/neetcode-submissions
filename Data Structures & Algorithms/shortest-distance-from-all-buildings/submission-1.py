class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        matrix = [[0] * C for _ in range(R)]

        def flood(r, c):
            dist = [[float("inf")] * C for _ in range(R)]
            q = deque([(r, c, 0)])
            while q:
                r, c, d = q.popleft()
                if d >= dist[r][c]:
                    continue
                dist[r][c] = d
                for nr, nc in [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)]:
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if grid[nr][nc] != 0:
                        continue
                    q.append((nr, nc, d + 1))

            for r in range(R):
                for c in range(C):
                    matrix[r][c] += dist[r][c]

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    flood(r, c)
        
        res = float("inf")
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 0:
                    continue
                res = min(res, matrix[r][c])
        if res == float("inf"):
            return -1
        return res
        