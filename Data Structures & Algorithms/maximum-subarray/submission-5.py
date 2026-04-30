class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        M = float("-inf")
        m = float("inf")
        v = 0
        for num in nums:
            v += num
            if v > M:
                M = v
            if v < m:
                m = v
        return M - m