class Solution:
    def largestRectangleArea(self, hs: List[int]) -> int:
        s = []
        M = 0
        for i, h in enumerate(hs):
            ni = i
            nh = h
            while s and s[-1][1] > h:
                ni, nh = s.pop()
            if not s or s[-1][1] < h:
                s.append((ni, min(h, nh)))
            for j, j_h in s:
                w = i - j + 1
                M = max(M, j_h * w)
        return M