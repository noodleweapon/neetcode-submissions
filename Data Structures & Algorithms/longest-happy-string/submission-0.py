class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a > 0:
            heapq.heappush(h, (-a ,'a'))
        if b > 0:
            heapq.heappush(h, (-b ,'b'))
        if c > 0:
            heapq.heappush(h, (-c ,'c'))

        s = ''
        while h:
            (f, c) = heapq.heappop(h)
            if len(s) > 1 and s[-2:] == c * 2:
                if not h:
                    break
                (f2, c2) = heapq.heappop(h)
                s += c2
                if f2 < -1:
                    heapq.heappush(h, (f2 + 1, c2))
            s += c
            if f < -1:
                heapq.heappush(h, (f + 1, c))
        
        return s