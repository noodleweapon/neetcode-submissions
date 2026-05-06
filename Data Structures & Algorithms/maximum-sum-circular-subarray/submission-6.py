class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        M = 0
        s = 0
        l = 0
        for r in range(2 * n):
            if r == l + n:
                break
            s += nums[r % n]
            if s <= 0:
                s = 0
                l = r + 1
                continue
            M = max(M, s)
        
        return M