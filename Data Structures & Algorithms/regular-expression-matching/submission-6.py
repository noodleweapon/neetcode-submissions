class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def eq(a, b):
            if b == '.':
                return True
            return a == b

        def rec(i1, i2):
            if i1 == len(s) and i2 == len(p):
                return True
            if i1 == len(s) or i2 == len(p):
                return False
            if eq(s[i1], p[i2]) and rec(i1 + 1, i2 + 1):
                return True
            if i2 < len(p) - 1 and p[i2 + 1] == '*':
                if rec(i1, i2 + 2):
                    return True
                if s[i1] == p[i2]:
                    return rec(i1 + 1, i2)
            return False
        
        return rec(0, 0)