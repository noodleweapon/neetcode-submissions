class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        h = [(0,0,0)]
        effort = [[float("inf")] * C for _ in range(R)]
        effort[0][0] = 0

        while h:
            (cost, r, c) = heapq.heappop(h)
            if cost > effort[r][c]:
                continue

            for (dr, dc) in [(-1,0), (1,0), (0, -1), (0,1)]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue

                pred_effort = max(cost, abs(heights[nr][nc] - heights[r][c]))
                if effort[nr][nc] > pred_effort:
                    effort[nr][nc] = pred_effort
                    heapq.heappush(h, (pred_effort, nr, nc))
        return effort[R - 1][C - 1]

        # [1,2,1,1,1]
        # [1,2,1,2,1]
        # [1,2,1,2,1]
        # [1,2,1,2,1]
        # [1,1,1,2,1]

