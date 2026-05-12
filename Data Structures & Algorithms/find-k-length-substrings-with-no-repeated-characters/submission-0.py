class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        d = defaultdict(int)
        l = 0
        res = 0
        for r in range(n):
            d[s[r]] += 1
            while r - l + 1 > k or d[s[r]] >= 2:
                d[s[l]] -= 1
                l += 1
            
            if r - l + 1 == k:
                res += 1
        return res