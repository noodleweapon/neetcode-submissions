class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        M = 0
        N = defaultdict(int)
        L = defaultdict(int)
        
        # AAABABB
        # BAAAB

        for r, c in enumerate(list(s)):
            def length():
                return r - L[c] + 1
            N[c] += 1
            while length() - N[c] > k:
                if s[L[c]] == c:
                    N[c] -= 1
                L[c] += 1
            
            M = max(M, length())
        for c in N:
            length = len(s) - L[c]
            if length - N[c] <= k:
                M = max(M, length)

        return M