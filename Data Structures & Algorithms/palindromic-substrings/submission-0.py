class Solution:
    def countSubstrings(self, s: str) -> int:
        n = 0
        for i in range(len(s)):
            for l, r in [[i, i], [i, i+1]]:
                while l >= 0 and r < len(s) and s[l] == s[l]:
                    l -= 1
                    r += 1