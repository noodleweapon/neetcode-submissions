class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def eq(a, b):
            if b == '.':
                return True
            return a == b
        memo = {}
        def rec(i, j):
            if j >= len(p):
                return i >= len(s)

            key = (i, j)
            if key in memo:
                return memo[key]
            
            match = i < len(s) and eq(s[i], p[j])
            if match and rec(i + 1, j + 1):
                memo[key] = True
                return True
            
            if j < len(p) - 1 and p[j + 1] == '*':
                if rec(i, j + 2):
                    memo[key] = True
                    return True
                if match and rec(i + 1, j):
                    memo[key] = True
                    return True
            memo[key] = False
            return False
            
        return rec(0, 0)