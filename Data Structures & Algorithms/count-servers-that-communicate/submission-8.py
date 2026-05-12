# class UnionFind:
#     def __init__(self, R, C):
#         self.rank = [[] * C for _ in range(R)]
#         self.par = [[] * C for _ in range(R)]

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        
        rows = [sum(grid[r]) for r in range(R)]
        cols = [sum([grid[r][c] for r in range(R)]) for c in range(C)]

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                if rows[r] > 1 or cols[c] > 1:
                    res += 1
        
        return res

        