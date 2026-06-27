class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        heights = [0] * C
        area = 0
        for row in matrix:
            for c in range(C):
                if row[c] == 0:
                    heights[c] = 0
                else:
                    heights[c] += 1
            
            w = 0
            for h in reversed(sorted(heights)):
                w += 1
                area = max(area, h * w)

        return area