class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(list(s))
        h = [(-f, c) for c, f in c.items()]
        heapq.heapify(h)

        s = ""
        while h:
            (neg_f, c) = heapq.heappop(h)
            s += c
            if neg_f == -1: # was last char of this type
                continue # start again.
            elif neg_f < -1: # has more of this type
                if not h: # no other char to interleave.
                    return "" # fail
            (neg_f2, c2) = heapq.heappop(h) # the other char
            s += c2

            if neg_f < -1:
                heapq.heappush(h, (neg_f + 1, c))
            if neg_f2 < -1:
                heapq.heappush(h, (neg_f2 + 1, c2))
        
        return s