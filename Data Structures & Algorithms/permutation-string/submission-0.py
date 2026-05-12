class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = defaultdict(int)
        for c in s1:
            s1dict[c] += 1

        d = defaultdict(int)
        q = deque([])

        for c in s2:
            q.append(c)
            d[c] += 1
            if len(q) > len(s1):
                popc = q.popleft()
                d[popc] -= 1
                if d[popc] <= 0:
                    d.pop(popc)

            if d == s1dict:
                return True
        return False