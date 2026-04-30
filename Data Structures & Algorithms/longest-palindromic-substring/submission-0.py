class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        m = ""
        for i in range(1, len(s) - 1):
            for r in [0, 1]:
                l = 0
                while i - l >= 0 and i + l + r < len(s) and s[i - l] == s[i + l + r]:
                    l += 1
                if l > len(m):
                    m = s[i - l:i + l + r - 1]

        return m