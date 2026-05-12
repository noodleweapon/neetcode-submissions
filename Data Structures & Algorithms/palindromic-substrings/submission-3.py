class Solution:
    def countSubstrings(self, s: str) -> int:
        C = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                C += 1
                l -= 1
                r += 1
        
        for i in range(len(s) - 1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                C += 1
                l -= 1
                r += 1
        
        return C