class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        H = 0
        n = len(heights)
        s = []
        for i in reversed(range(n)):
            h = heights[i]
            if h > H:
                s.append(i)
            H = max(H, h)

        s.reverse()
        return s