class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        visited = set()
        q = deque([(0,0)])
        dp = [[float("inf")] * C for _ in range(R)]
        dp[0][0] = 0

        while q:
            (r, c) = q.popleft()
            for (dr, dc) in [(-1,0), (1,0), (0, -1), (0,1)]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue
                if dp[nr][nc] != float("inf"):
                    cost = max(dp[nr][nc], abs(heights[nr][nc] - heights[r][c]))
                    if cost < dp[r][c]:
                        dp[r][c] = cost
                        q.append((r, c))
                if (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                q.append((nr, nc))

        return dp[R - 1][C-1]

        # [1,2,1,1,1]
        # [1,2,1,2,1]
        # [1,2,1,2,1]
        # [1,2,1,2,1]
        # [1,1,1,2,1]

