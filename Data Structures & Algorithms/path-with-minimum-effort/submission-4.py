class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        visited = set((0, 0))
        h = [(0, (0, 0))]

        while h:
            effort, coord = heapq.heappop(h)
            if coord == (R - 1, C - 1):
                return effort
            r, c = coord
            if coord in visited:
                continue
            visited.add(coord)
            height1 = heights[r][c]
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    next_coord = (nr, nc)
                    if next_coord in visited:
                        continue

                    height2 = heights[nr][nc]
                    nextEffort = max(effort, abs(height2 - height1))
                    heapq.heappush(h, (nextEffort, next_coord))

