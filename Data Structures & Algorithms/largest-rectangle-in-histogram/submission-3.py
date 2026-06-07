class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        M = 0
        s = []
        for i, h in enumerate(heights):
            j = i
            while s and s[-1][1] >= h:
                j = s[-1][0]
                s.pop()
            s.append((j, h))
            for (k, height) in s:
                area = min(h, height) * (i - k + 1)
                M = max(M, area)

        return M


        # 7,1,7,2,2,4