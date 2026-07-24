class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        D = {}
        usedRightSide = set()
        n, m = len(s), len(pattern)

        def rec(i, j):
            if i == n and j == m:
                print(list(usedRightSide))
                return True
            if i == n or j == m:
                return False
            
            # Bug: when a pattern character already has a mapping, you must verify that s[i:] starts with it.
            if pattern[j] in D:
                if not s[i:].startswith(D[pattern[j]]):
                    return False
                return rec(i + len(D[pattern[j]]), j + 1)

            for iNext in range(i + 1, n + 1):
                text = s[i:iNext]
                if text in usedRightSide:
                    continue
                usedRightSide.add(text)
                D[pattern[j]] = text
                if rec(iNext, j + 1):
                    return True
                D.pop(pattern[j])
                usedRightSide.discard(text)
            return False
        
        return rec(0, 0)