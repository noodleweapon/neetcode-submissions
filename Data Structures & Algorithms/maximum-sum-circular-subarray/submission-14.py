class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        M = min(nums)
        s = 0
        l = 0
        for r in range(2 * n):
            s += nums[r % n]
            while l + n <= r:
                s -= nums[l % n]
                l += 1
            M = max(M, s)
            if s < 0:
                l = r + 1
                s = 0
        
        return M