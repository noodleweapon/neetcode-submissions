class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        R, C = len(maze), len(maze[0])
        h = [(0, *start)]
        dist = [[float("inf") for _ in range(C)] for _ in range(R)]
        while h:
            cost, r, c = heapq.heappop(h)
            if (r, c) == tuple(destination):
                return cost
            if cost >= dist[r][c]:
                continue
            dist[r][c] = cost

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r, c
                delta = 0
                while True:
                    nr += dr
                    nc += dc
                    if not (0 <= nr < R and 0 <= nc < C) or maze[nr][nc] == 1:
                        nr -= dr
                        nc -= dc
                        break
                    delta += 1
                if delta == 0:
                    continue
                if cost + delta >= dist[nr][nc]:
                    continue
                h.append((cost + delta, nr, nc))
        
        return -1