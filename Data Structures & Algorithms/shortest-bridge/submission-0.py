class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        SCC = [[0] * C for _ in range(R)]
        scc_counter = 1
        q1, q2 = deque(), deque()

        def dfs(q, r, c):
            SCC[r][c] = scc_counter
            q.append((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nc < 0 or nr < 0 or nc >= C or nr >= R:
                    continue
                if grid[nr][nc] == 0:
                    continue
                if SCC[nr][nc] != 0:
                    continue
                dfs(q, nr, nc)

        for r in range(R):
            for c in range(C):
                if SCC[r][c] == 0 and grid[r][c] == 1:
                    q = q1 if scc_counter == 1 else q2
                    dfs(q, r, c)
                    scc_counter *= -1

        bridge = 0
        while True:
            scc_num = 1 if bridge % 2 else -1
            q = q1 if bridge % 2 else q2
            bridge += 1

            if not q:
                return bridge - 1
            for _ in range(len(q)):
                (r, c) = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr = r + dr
                    nc = c + dc
                    if nc < 0 or nr < 0 or nc >= C or nr >= R:
                        continue
                    if grid[nr][nc] == 1:
                        continue
                    if SCC[nr][nc] == -1 * scc_num:
                        return bridge - 1
                    if SCC[nr][nc] == scc_num:
                        continue
                    SCC[nr][nc] = scc_num
                    q.append((nr, nc))
        