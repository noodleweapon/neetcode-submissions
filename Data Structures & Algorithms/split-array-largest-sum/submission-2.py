class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        def cond(m):
            buckets = 0
            capacity = 0
            for num in nums:
                if capacity - num < 0:
                    buckets += 1
                    if buckets > k:
                        return False
                    capacity = m
                capacity -= num
            return True

        while l < r:
            m = (l + r) // 2
            if cond(m):
                r = m
            else:
                l = m + 1
        
        return l





        # [1,0,2,3,5], k = 4
