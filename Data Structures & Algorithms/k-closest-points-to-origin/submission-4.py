import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            d = math.pow(x, 2) + math.pow(y, 2)
            heapq.heappush(heap, (-d, [x, y]))
        # res = heapq.nsmallest(k, arr)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap))
        return list(map(lambda e : e[1], heap[:k]))