class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        m = 0
        for i, h in enumerate(heights):
            si = i
            while s and s[-1][1] > h:
                top = s.pop()
                a = top[1] * (i - top[0])
                m = max(m, a)
                si = top[0]
            
            if not s or s[-1][1] != h:
                s.append((si, h))
        
        print(s)
        while s:
            top = s.pop()
            a = top[1] * (len(heights) - top[0])
            m = max(m, a)
        
        return m