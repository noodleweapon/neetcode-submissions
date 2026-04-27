class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Q = deque([])
        R = len(grid)
        C = len(grid[0])
        fresh = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    Q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        t = 0
        while Q:
            l = len(Q)
            ticked = False
            for _ in range(l):
                (r, c) = Q.popleft()
                for (dr, dc) in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    nr = r + dr
                    nc = c + dc
                    if nc < 0 or nr < 0 or nc >= C or nr >= R:
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    ticked = True
                    fresh -= 1
                    Q.append((nr, nc))
            if ticked:
                t += 1

        if fresh == 0:
            return t
        else:
            return -1