class Solution:
    def reorganizeString(self, s: str) -> str:
        h = [(-f, c) for c, f in Counter(s).items()]
        heapq.heapify(h)
        res = ""
        q = None
        while h:
            neg_f, c = heapq.heappop(h)
            if q:
                heapq.heappush(h, q)
                q = None
            res += c
            if neg_f < -1:
                q = (neg_f + 1, c)

        if q:
            return ""
        return res