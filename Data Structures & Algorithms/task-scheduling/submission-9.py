class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        h = [-v for v in d.values()]
        heapq.heapify(h)
        q = deque()

        t = -1
        while h or q:
            t += 1
            if q and q[0][0] == t:
                (_t, _v) = q.popleft()
                heapq.heappush(h, _v)
            if h:
                v = heapq.heappop(h) + 1
                if v < 0: # this was my mistake.
                    q.append((t + n + 1, v)) # and this, +1

        return t + 1