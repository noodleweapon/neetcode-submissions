class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        h = []
        for i in range(n - 1):
            heapq.heappush(h, weights[i] + weights[i + 1])
        
        maxS = sum(heapq.nlargest(k - 1, h))
        minS = sum(heapq.nsmallest(k - 1, h))
        return maxS - minS