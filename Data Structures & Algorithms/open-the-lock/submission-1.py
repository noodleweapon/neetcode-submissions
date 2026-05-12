class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        n = len(target)
        q = deque(["0000"])
        visited = set(deadends)
        if "0000" in visited:
            return -1

        d = -1
        while q:
            d += 1
            for _ in range(len(q)):
                s = q.popleft()
                if s == target:
                    return d
                for i in range(0, 4):
                    a = str((int(s[i]) + 1) % 10)
                    b = str((int(s[i]) + 9) % 10)
                    a = s[:i] + a + s[i+1:]
                    b = s[:i] + b + s[i+1:]
                    if a not in visited:
                        visited.add(a)
                        q.append(a)
                    if b not in visited:
                        visited.add(b)
                        q.append(b)
        return -1