# class UnionFind:
#     def __init__(self, R, C):
#         self.rank = [[] * C for _ in range(R)]
#         self.par = [[] * C for _ in range(R)]

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        counted = [[False] * C for _ in range(R)]

        conn = 0
        for r in range(R):
            S = sum(grid[r])
            if S < 2:
                continue
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                if counted[r][c]:
                    continue
                counted[r][c] = True
                conn += 1
        
        for c in range(C):
            S = 0
            for r in range(R):
                S += grid[r][c]
            if S < 2:
                continue
            for r in range(R):
                if grid[r][c] == 0:
                    continue
                if counted[r][c]:
                    continue
                counted[r][c] = True
                conn += 1
        
        return conn

        