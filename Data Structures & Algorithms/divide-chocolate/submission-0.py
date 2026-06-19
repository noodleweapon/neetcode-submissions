class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        groups = k + 1
        l, r = min(sweetness), sum(sweetness) // groups
        def cond(x):
            accum = 0
            count = 0
            for s in sweetness:
                accum += s
                if accum >= x:
                    accum = 0
                    count += 1
            return count >= groups

        while l < r:
            m = (l + r + 1) // 2
            if cond(m):
                l = m
            else:
                r = m - 1
        return l

        # [1,2,3,    4,5,   6,   7,   8,   9], k = 5
        # 6, 9, 6, 7, 8, 9
        # my ans = 6
        # let's say i tried 7: then all would be >= 7. Then can't fill 6 buckets.
