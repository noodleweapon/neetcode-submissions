class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        b = 0
        l = 0
        M = 0
        for r in range(n):
            if blocks[r] == 'B':
                b += 1
            if r - l + 1 > k:
                if blocks[l] == 'B':
                    b -= 1
                l += 1
            M = max(M, b)
        
        return max(0, k - M)

        # BBWWBBWB