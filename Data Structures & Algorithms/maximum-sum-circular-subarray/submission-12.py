class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        M = min(nums)
        s = 0
        l = 0
        for r in range(2 * n):
            while l + n <= r:
                s -= nums[l % n]
                l += 1
            if s < 0:
                l = r
                s = 0
            s += nums[r % n]
            M = max(M, s)
        
        return M