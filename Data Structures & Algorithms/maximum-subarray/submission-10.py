class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M = float("-inf")
        m = 0
        v = 0
        for num in nums:
            v += num
            M = max(M, v - m)
            m = min(m, v)
        return M