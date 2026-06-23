class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(pr, pc, pdr, pdc):
            grid[pr][pc] = 0
            shape = []
            shape.append((pdr, pdc))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = pr + dr, pc + dc
                if (0 <= nr < R) and (0 <= nc < C) and grid[nr][nc] == 1:
                    for _r, _c in dfs(nr, nc, dr, dc):
                        shape.append((_r + pdr, _c + pdc))
            return shape

        shapes = set()
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    shape = tuple(dfs(r, c, 0, 0))
                    if shape not in shapes:
                        res += 1
                    shapes.add(shape)
        return res
