class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        d = {}
        res = 0
        while r < len(s):
            rc = s[r]
            while rc in d:
                lc = s[l]
                d.pop(lc)
                l += 1
            d[rc] = True
            r += 1
            res = max(res, r - l)
        return res