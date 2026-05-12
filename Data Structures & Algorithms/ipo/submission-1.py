class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits) #
        inds = list(range(n))
        inds.sort(key=lambda x: capital[x]) #

        h, idx = [], 0
        for _ in range(k):
            while idx < n and capital[inds[idx]] <= w:
                heapq.heappush(h, -1 * profits[inds[idx]])
                idx += 1
            if not h:
                break
            delta = -1 * heapq.heappop(h)
            w += delta

        return w