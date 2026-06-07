class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        M = 0
        s = []
        for i, h in enumerate(heights):
            j = i
            while s and s[-1][1] > h:
                j, old_h = s.pop()
                area = old_h * (i - j)
                M = max(M, area)
            if s and s[-1][1] == h:
                continue
            s.append((j, h))

        return M


        # 7,1,7,2,2,4