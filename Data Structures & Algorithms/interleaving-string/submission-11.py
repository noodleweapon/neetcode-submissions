class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        
        arr = deque([(0, 0)])
        for i3 in range(n3):
            seen = set()
            for _ in range(len(arr)):
                (i1, i2) = arr.popleft()
                if i2 < n2 and s2[i2] == s3[i3]:
                    if (i1, i2 + 1) not in seen:
                        arr.append((i1, i2 + 1))
                        seen.add((i1, i2 + 1))
                if i1 < n1 and s1[i1] == s3[i3]:
                    if (i1 + 1, i2) not in seen:
                        arr.append((i1 + 1, i2))
                        seen.add((i1 + 1, i2))
        
        return bool(arr)