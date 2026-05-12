class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M = nums[0]
        s = 0
        for i in range(len(nums)):
            s = max(nums[i], s + nums[i])
            M = max(M, s)
        return M