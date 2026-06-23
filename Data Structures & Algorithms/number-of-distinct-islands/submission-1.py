class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c, rr, cc):
            grid[r][c] = 0
            shape = []
            shape.append((r - rr, c - cc))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < R) and (0 <= nc < C) and grid[nr][nc] == 1:
                    for _r, _c in dfs(nr, nc, rr, cc):
                        shape.append((_r, _c))
            return shape

        shapes = set()
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    shape = tuple(dfs(r, c, r, c))
                    if shape not in shapes:
                        res += 1
                    shapes.add(shape)
        return res
