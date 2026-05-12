class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        cost = [[float("inf")] * C for _ in range(R)]
        cost[0][0] = grid[0][0]
        h = [(grid[0][0], 0, 0)]

        while h:
            d, r, c = heapq.heappop(h)
            if d > cost[r][c]:
                continue
            
            for (nr, nc) in [(r + 1, c), (r, c + 1)]:
                if nc > C - 1 or nr > R - 1:
                    continue
                D = d + grid[nr][nc]
                if D < cost[nr][nc]:
                    cost[nr][nc] = D
                    heapq.heappush(h, (D, nr, nc))
        
        return cost[R - 1][C - 1]