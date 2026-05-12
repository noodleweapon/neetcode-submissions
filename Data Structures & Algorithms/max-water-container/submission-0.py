class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        li = 0
        ri = len(heights) - 1
        while ri > li:
            rh = heights[ri]
            lh = heights[li]
            a = (ri - li) * min(rh, lh)
            if a > m:
                m = a
            if rh > lh:
                li += 1
            else:
                ri -= 1
        return m
