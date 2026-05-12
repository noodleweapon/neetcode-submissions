class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        M = 0
        while i < j:
            L = heights[i]
            R = heights[j]
            area = (j - i) * min(L, R)
            if area > M:
                M = area
            
            if L < R:
                i += 1
            else:
                j -= 1
        return M