class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_subarr = 0
        n = len(nums)
        s = 0
        for i in range(n):
            s += nums[i]
            if s >= 0:
                s = 0
                continue
            min_subarr = min(min_subarr, s)
        if min_subarr == 0:
            return max(nums)
        return max(max(nums), sum(nums) - min_subarr)
