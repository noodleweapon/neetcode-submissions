class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        q = deque([])
        h = [(-f, c) for c, f in Counter(s).items()]
        heapq.heapify(h)
        res = ''
        i = 0
        while h or q:
            if q and q[0][0] <= i:
                _, neg_f, c = q.popleft()
                heapq.heappush(h, (neg_f, c))
            if not h:
                return ""
            neg_f, c = heapq.heappop(h)
            res += c
            if neg_f <= -2:
                q.append((i + k, neg_f + 1, c))
            i += 1
        return res
