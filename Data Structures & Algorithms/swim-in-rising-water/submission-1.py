class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = [(grid[0][0], 0, 0)]
        n = len(grid)
        visited = set()
        while h:
            (t, r, c) = heapq.heappop(h)
            if r == n - 1 and c == n - 1:
                return t
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nc < 0 or nr < 0 or nc >= n or nr >= n:
                    continue
                if (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                nt = grid[nr][nc]
                heapq.heappush(h, (max(nt, t), nr, nc))
