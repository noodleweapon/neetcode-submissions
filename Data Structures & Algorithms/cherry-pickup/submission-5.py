class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = {}
        def dfs(r1, c1, r2, c2):
            if r1 == c1 == r2 == c2 == n - 1:
                return grid[n - 1][n - 1]
            key = (r1, c1, r2, c2)
            if key in dp:
                return dp[key]

            res = float("-inf")
            if r1 == r2 and c1 == c2:
                cur = grid[r1][c1]
            else:
                cur = grid[r1][c1] + grid[r2][c2]
            for _r1, _c1 in [(r1, c1 + 1), (r1 + 1, c1)]:
                for _r2, _c2 in [(r2, c2 + 1), (r2 + 1, c2)]:
                    if not (0 <= _r1 < n and 0 <= _c1 < n):
                        continue
                    if not (0 <= _r2 < n and 0 <= _c2 < n):
                        continue
                    if grid[_r1][_c1] == -1 or grid[_r2][_c2] == -1:
                        continue
                    res = max(res, cur + dfs(_r1, _c1, _r2, _c2))
            dp[key] = res
            return res
        
        return max(0, dfs(0, 0, 0, 0))