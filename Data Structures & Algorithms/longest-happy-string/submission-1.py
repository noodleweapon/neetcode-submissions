class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        h = []
        if a > 0:
            heapq.heappush(h, (-a, 'a'))
        if b > 0:
            heapq.heappush(h, (-b, 'b'))
        if c > 0:
            heapq.heappush(h, (-c, 'c'))
        q = None
        while h:
            neg_f, c = heapq.heappop(h)
            if q:
                heapq.heappush(h, q)
                q = None
            res += c
            if neg_f == -1:
                continue
            
            if len(res) > 1 and res[-1] == c and res[-2] == c:
                q = (neg_f + 1, c)
            else:
                heapq.heappush(h, (neg_f + 1, c))
        return res