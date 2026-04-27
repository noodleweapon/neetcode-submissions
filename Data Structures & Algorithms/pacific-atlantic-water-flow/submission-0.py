class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])

        def get_grid(init_r, init_c):
            Q = deque([])
            for c in range(C):
                Q.append((init_r, c))
            for r in range(R):
                Q.append((r, init_c))

            grid = [[False] * C for i in range(R)]

            while Q:
                l = len(Q)
                for _ in range(l):
                    (r, c) = Q.popleft()
                    print(r, c)
                    if grid[r][c]:
                        continue
                    grid[r][c] = True
                    for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr = r + dr
                        nc = c + dc
                        if nr < 0 or nc < 0 or nr >= R or nc >= C:
                            continue
                        if heights[nr][nc] < heights[r][c]:
                            continue
                        Q.append((nr, nc))
            return grid
        
        res = []
        pacific = get_grid(0, 0)
        atlantic = get_grid(R - 1, C - 1)
        for r in range(R):
            for c in range(C):
                if pacific[r][c] and atlantic[r][c]:
                    res.append((r, c))
        return res