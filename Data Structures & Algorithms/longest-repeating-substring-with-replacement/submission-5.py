from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = defaultdict(int)
        K = defaultdict(int)
        letters = set(list(s))
        M = 0

        for r, c in enumerate(s):
            for letter in letters:
                if letter == c:
                    continue
                
                K[letter] += 1
                while L[letter] <= r and K[letter] > k:
                    l = L[letter]
                    L[letter] += 1
                    if l == letter:
                        K[letter] -= 1
            M = max(M, r - L[c] + 1)
        
        return M