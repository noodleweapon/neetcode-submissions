class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R, C = len(maze), len(maze[0])
        # 9:15 - 9:45
        visited = set()
        def dfs(r, c, dr, dc):
            key = (r, c, dr, dc)
            if key in visited:
                return False
            visited.add(key)
            if (r, c) == (*destination,):
                return True

            while True:
                r += dr
                c += dc
                if not(0 <= r < R and 0 <= c < C) or maze[r][c] == 1:
                    r -= dr
                    c -= dc
                    break
            
            for ddr, ddc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (ddr, ddc) == (dr, dc) or (ddr, ddc) == (-dr, -dc):
                    continue
                if dfs(r, c, ddr, ddc):
                    return True

            return False

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dfs(*start, dr, dc):
                return True
            
        return False
        