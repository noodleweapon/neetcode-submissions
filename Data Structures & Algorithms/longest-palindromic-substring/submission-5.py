class Solution:
    def longestPalindrome(self, s: str) -> str:
        M = 0
        L = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l > M:
                    M = r - l
                    L = l
                l -= 1
                r += 1

        for i in range(len(s) - 1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l > M:
                    M = r - l
                    L = l
                l -= 1
                r += 1
        
        return s[L:L+M+1]