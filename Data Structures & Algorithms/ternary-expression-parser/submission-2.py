class Solution:
    def parseTernary(self, t: str) -> str:
        n = len(t)
        s = []
        for i in reversed(range(n)):
            if s and s[-1] == '?':
                is_true = t[i] == 'T'
                s.pop() # ?
                T = s.pop() # F
                s.pop() # :
                F = s.pop() # T
                s.append(T if is_true else F)
            else:
                s.append(t[i])
        return s[0]