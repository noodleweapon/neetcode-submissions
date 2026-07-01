class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []
        def find(h):
            l, r = 0, len(stack) - 1
            while l < r:
                m = (l + r + 1) // 2
                if stack[m] >= h:
                    l = m
                else:
                    r = m - 1
            return len(stack) - l

        for i in reversed(range(n)):
            h = heights[i]
            res[i] = find(h)
            while stack and stack[-1] <= h:
                stack.pop()
            stack.append(h)
        return res

        # 3,1,5,8,6

        # 10,6,8,5,11,9