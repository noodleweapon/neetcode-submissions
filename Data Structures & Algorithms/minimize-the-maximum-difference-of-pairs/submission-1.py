class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: # empty set
            return 0
        n = len(nums)
        nums.sort() # ascending

        def cond(x):
            print(x)
            f = i = 0 # num possible pairs, index
            while i < n - 1:
                if abs(nums[i] - nums[i + 1]) > x:
                    i += 1
                else:
                    f += 1
                    i += 2
            return f >= p

        l, r = 0, nums[-1] - nums[0]

        while l < r:
            m = (l + r) // 2
            if cond(m):
                r = m
            else:
                l = m + 1
        return r


        # 1,2,2,10,11

        # [1,1,2,3,7,10], p=2

