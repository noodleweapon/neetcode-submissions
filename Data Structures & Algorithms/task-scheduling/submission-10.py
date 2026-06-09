class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        h = [-f for task, f in c.items()]
        heapq.heapify(h)
        q = deque([])
        t = 0
        while h or q:
            if q and q[0][0] == t:
                avai_at_t, neg_f = q.popleft()
                heapq.heappush(h, neg_f)

            if h:
                neg_f = heapq.heappop(h) + 1
                if neg_f < 0:
                    q.append((t + n + 1, neg_f))
            t += 1

        return t

        # ["X","X","Y","Y"]