class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def rec(i1, i2):
            if i1 == len(s) and i2 == len(p):
                return True
            if i1 == len(s) or i2 == len(p):
                return False
            
            if s[i1] == p[i2] or p[i2] == '.':
                if rec(i1 + 1, i2 + 1):
                    return True

            if p[i2] == '*':
                if rec(i1 + 1, i2):
                    return True
                if rec(i1 + 1, i2 + 1):
                    return True
            
            return False
        
        return rec(0, 0)