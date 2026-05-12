class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        cost = [[-1] * C for _ in range(R)]
        cost[0][0] = grid[0][0]
        for c in range(1, C):
            cost[0][c] = grid[0][c] + cost[0][c - 1]
        for r in range(1, R):
            cost[r][0] = grid[r][0] + cost[r - 1][0]
        
        for r in range(1, R):
            for c in range(1, C):
                sp = min(cost[r - 1][c], cost[r][c - 1])
                cost[r][c] = sp + grid[r][c]
        
        return cost[R - 1][C - 1]