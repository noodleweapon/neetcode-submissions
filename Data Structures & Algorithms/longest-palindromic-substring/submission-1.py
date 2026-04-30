class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        m = ""
        for i in range(len(s)):
            for l, r in [[i, i], [i, i + 1]]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    d = r - l
                    if d > len(m):
                        m = s[l:r+1]
                    l -= 1
                    r += 1
        return m