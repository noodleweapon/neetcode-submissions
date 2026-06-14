class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        water = [[float("inf")] * C for _ in range(R)]
        # water[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        while heap:
            w, r, c = heapq.heappop(heap)
            if w >= water[r][c]:
                continue
            water[r][c] = w

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    nw = max(w, grid[nr][nc])
                    if nw >= water[nr][nc]:
                        continue
                    heapq.heappush(heap, (nw, nr, nc))

        return water[R - 1][C - 1]

#   [0,1,2,10],
#   [9,14,4,13],
#   [12,3,8,15],
#   [11,5,7,6]