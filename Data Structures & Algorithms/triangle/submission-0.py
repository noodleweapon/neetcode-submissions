class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        for r in reversed(range(N - 1)): # Was missing reversed
            for c in range(len(triangle[r])):
                triangle[r][c] += min([
                    triangle[r + 1][c],
                    triangle[r + 1][c + 1]
                ])
        return triangle[0][0]