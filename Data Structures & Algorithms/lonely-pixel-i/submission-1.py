class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        R = len(picture)
        C = len(picture[0])

        def Bsum(arr):
            z = 0
            for item in arr:
                if item == 'B':
                    z += 1
            return z

        rows = [Bsum(picture[r]) for r in range(R)] # len R
        cols = [Bsum([picture[r][c] for r in range(R)]) for c in range(C)] # len C

        res = 0
        for r in range(R):
            for c in range(C):
                if picture[r][c] != 'B':
                    continue
                if rows[r] > 1 or cols[c] > 1:
                    continue
                res += 1
        
        return res