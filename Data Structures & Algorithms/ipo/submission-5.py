class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pc = [(p, c) for p, c in zip(profits, capital)]
        pc.sort(key=lambda x: x[1])
        pc_i, pc_n = 0, len(pc)
        h = []
        for _ in range(k):
            while pc_i < pc_n and pc[pc_i][1] <= w:
                heapq.heappush(h, -pc[pc_i][0])
                pc_i += 1
            if not h:
                break
            w -= heapq.heappop(h)

        return w
