class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cond(v):
            t = 0
            c = 0
            for num in nums:
                if t - num < 0:
                    t = v
                    c += 1
                    if c > k:
                        return False
                t -= num
            return True

        # find the smallest that works.
        r = sum(nums)
        l = max(max(nums), r // k)
        while l < r:
            m = (l + r) // 2
            if cond(m):
                r = m
            else:
                l = m + 1
        return l
        
        # contiguous part of the array.

        # [2,4,10,1,5]


        # [1, 5]
        # [2,4,10]