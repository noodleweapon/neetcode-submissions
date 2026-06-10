class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pc = [(p, c) for p, c in zip(profits, capital)]
        pc.sort(key=lambda x: x[1])
        pc_i, pc_n = 0, len(pc)
        h = []
        while h or pc_i < pc_n:
            if k == 0:
                break
            while pc_i < pc_n and pc[pc_i][1] <= w:
                heapq.heappush(h, -pc[pc_i][0])
                pc_i += 1
            if not h:
                break
            w -= heapq.heappop(h)
            k -= 1

        return w
