class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def eq(a, b):
            if b == '.':
                return True
            return a == b

        def rec(i, j):
            if j >= len(p):
                return i >= len(s)
            
            if i < len(s) and eq(s[i], p[j]) and rec(i + 1, j + 1):
                return True
            
            if j < len(p) - 1 and p[j + 1] == '*':
                return rec(i, j + 2) or rec(i + 1, j)
            
            return False
            
        return rec(0, 0)