class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        matrix = [[float("-inf") for _ in range(C)] for _ in range(R)]
        h = [(-grid[0][0], 0, 0)]
        while h:
            neg_score, r, c = heapq.heappop(h)
            score = -neg_score
            if score <= matrix[r][c]:
                continue
            matrix[r][c] = score
            if (r, c) == (R - 1, C - 1):
                return score
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (0 <= nr < R) and (0 <= nc < C):
                    new_score = min(score, grid[nr][nc])
                    if matrix[nr][nc] >= new_score:
                        continue
                    heapq.heappush(h, (-new_score, nr, nc))


        # 511
        # 116=1