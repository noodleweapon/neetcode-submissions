class Solution:
    def parseTernary(self, expression: str) -> str:
        s = []
        i = 0
        while i < len(expression):
            c = expression[i]
            if c == 'T':
                s.append('T')
            if c == 'F':
                s.append('F')
            elif c == '?':
                if s[-1] == 'T':
                    s[-1] = expression[i + 1]
                    i += 1
            elif c == ':':
                if s[-1] == 'F':
                    s[-1] = expression[i + 1]
                    i += 1
            
            i += 1
            
        return s[0]
