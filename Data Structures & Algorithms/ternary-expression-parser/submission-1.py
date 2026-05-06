class Solution:
    def parseTernary(self, t: str) -> str:
        s = []
        i = 0
        while i < len(t):
            print(s)
            if i + 1 < len(t):
                print(t[i:i+1])
                if t[i:i+1] == 'T?':
                    s.append('T?')
                    i += 2
                    continue
                elif t[i:i+1] == 'F?':
                    s.append('F?')
                    i += 2
                    continue
            if t[i] == ':':
                T = s.pop()
                F = t[i]
                i += 2
                isTrue = s.pop() == 'T?'
                if isTrue:
                    s.append(T)
                else:
                    s.append(F)
            else:
                s.append(t[i])
                i += 1
        print(s)
        return s[0]
