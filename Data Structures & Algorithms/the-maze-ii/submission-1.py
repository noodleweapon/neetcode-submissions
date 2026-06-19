class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        R, C = len(maze), len(maze[0])
        h = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            h.append((0, *start, dr, dc))
        
        dist = [[float("inf") for _ in range(C)] for _ in range(R)]
        dist[start[0]][start[1]] = 0
        while h:
            cost, r, c, dr, dc = heapq.heappop(h)
            if (r, c) == tuple(destination):
                return cost
            if cost > dist[r][c]:
                continue
            dist[r][c] = cost

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

            for ddr, ddc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (ddr, ddc) == (dr, dc) or (ddr, ddc) == (-dr, -dc):
                    continue
                if cost + delta >= dist[nr][nc]:
                    continue
                h.append((cost + delta, nr, nc, ddr, ddc))
        
        return -1