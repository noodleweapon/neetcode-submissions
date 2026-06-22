class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        R, C = len(costs), len(costs[0])
        h = []
        dist = [[float("inf")] * C for _ in range(R)]
        for c in range(C):
            item = (costs[0][c], 0, c)
            heapq.heappush(h, item)
        
        while h:
            cur_dist, r, c = heapq.heappop(h)
            if r == R - 1:
                return cur_dist
            if cur_dist >= dist[r][c]:
                continue
            dist[r][c] = cur_dist
            for i in range(C):
                if i == c:
                    continue
                new_dist = cur_dist + costs[r + 1][i]
                if new_dist < dist[r + 1][i]:
                    item = (new_dist, r + 1, i)
                    heapq.heappush(h, item)

        
        # costs: house | color (0,1,2,...k)
        # [1,5,3] <-- 1 here
        # [2,9,4]