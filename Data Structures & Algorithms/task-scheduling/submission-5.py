class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        h = [-v for v in d.values()]
        heapq.heapify(h)
        q = deque()

        t = 0
        while h or q:
            if q and q[0][0] == t:
                (_t, _v) = q.popleft()
                heapq.heappush(h, _v)
            if not h:
                t += 1
                continue
            v = heapq.heappop(h)
            if v < 0:
                q.append((t + n, v + 1))
                t += 1

        return t

# tasks=["A","A","A","B","C"]