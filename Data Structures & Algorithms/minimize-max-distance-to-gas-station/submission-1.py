class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        h = []
        n = len(stations)
        for i in range(n - 1):
            a, b = stations[i], stations[i + 1]
            heapq.heappush(h, ((a - b), 1, a - b))

        for _ in range(k):
            neg_d, denom, neg_numer = heapq.heappop(h)
            denom += 1
            heapq.heappush(h, (neg_numer / denom, denom, neg_numer))
        
        return -heapq.heappop(h)[0]