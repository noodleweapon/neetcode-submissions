from collections import defaultdict

class Solution:
    def isNonNeg(self, d) -> bool:
        for k, v in d.items():
            if v < 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for c in t:
            d[c] -= 1
        
        m_text = ""
        m_len = float("inf")

        l = r = 0
        while r < len(s):
            d[s[r]] += 1
            r += 1
            while d[s[l]] > 0 and l < r:
                d[s[l]] -= 1
                l += 1

            if self.isNonNeg(d):
                new_len = r - l
                if new_len < m_len:
                    m_len = new_len
                    m_text = s[l:r]
        return m_text
