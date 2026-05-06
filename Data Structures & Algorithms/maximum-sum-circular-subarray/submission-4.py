class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        min_subarr = 0
        s = 0
        for i in range(n):
            s += nums[i]
            if s >= 0:
                s = 0
                continue
            min_subarr = min(min_subarr, s)
        
        S = sum(nums)
        if S == min_subarr:
            return max(nums)
        return sum(nums) - min_subarr
