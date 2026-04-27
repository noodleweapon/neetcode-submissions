class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            x, y = point
            d = x * x + y * y
            pair = (d, point)
            heapq.heappush(h, pair)
        
        elems = heapq.nsmallest(k, h)
        out = [coord for d, coord in elems]
        return out