import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x, y in points:
            d = math.pow(x, 2) + math.pow(y, 2)
            arr.append((d, [x, y]))
        res = heapq.nsmallest(k, arr)
        return list(map(lambda e : e[1], res))