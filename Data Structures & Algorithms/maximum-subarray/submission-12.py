class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M = float("-inf")
        t = 0
        for num in nums:
            t = max(t + num, num)
            M = max(M, t)
        return M