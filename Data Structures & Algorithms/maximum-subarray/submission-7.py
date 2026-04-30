class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        M = float("-inf")
        m = 0
        v = 0
        for num in nums:
            v += num
            M = max(M, v)
            m = min(m, v)
        return M - m