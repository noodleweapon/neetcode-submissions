class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set()
        for i in range(1, 27):
            valid.add(str(i))

        a = 1
        b = 1
        for i in reversed(range(len(s))):
            c = 0
            if s[i] in valid:
                c += b
            if i + 1 < len(s):
                if (s[i] + s[i + 1]) in valid:
                    c += a
            
            a = b
            b = c
        
        return b