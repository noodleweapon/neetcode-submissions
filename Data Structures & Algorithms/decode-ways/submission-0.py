class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = 0
        i = len(s) - 1
        while i >= 0:
            if (1 <= int(s[i]) <= 26):
                n += 1
                i -= 1
                continue
            
            if i == 0:
                break
            if (1 <= int(s[i] + s[i - 1]) <= 26):
                n += 1
                i -= 2
        return n