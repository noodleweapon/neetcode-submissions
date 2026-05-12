from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = defaultdict(int)
        K = defaultdict(int)
        letters = set(list(s))
        M = 0

        for r, c in enumerate(s):
            for letter in letters:
                if letter != c:
                    K[letter] += 1
                while K[letter] > k:
                    if s[L[letter]] != letter:
                        K[letter] -= 1
                    L[letter] += 1
            M = max(M, r - L[c] + 1)
        
        for letter in letters:
            if K[letter] > k:
                continue
            M = max(M, len(s) - L[letter])
        return M