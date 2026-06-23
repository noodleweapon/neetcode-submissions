class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        E = defaultdict(set)
        E_rev = defaultdict(set)
        for a, b in relations:
            E[a].add(b)
            E_rev[b].add(a)
        seen = set()
        q = deque()
        for u in range(1, n + 1):
            if len(E_rev[u]) == 0:
                q.append(u)
                seen.add(u)
        sems = 0
        while q:
            sems += 1
            for _ in range(len(q)):
                u = q.popleft()
                for v in E[u]:
                    E_rev[v].discard(u)
                    if len(E_rev[v]) == 0 and v not in seen:
                        seen.add(v)
                        q.append(v)
        if len(seen) == n:
            return sems
        else:
            return -1