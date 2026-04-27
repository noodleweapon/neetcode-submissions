class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        M = curMin = curMax = nums[0]
        for n in nums[1:]:
            arg1 = curMax * n
            arg2 = curMin * n
            curMax = max(arg1, arg2, n)
            curMin = min(arg1, arg2, n)
            M = max(M, curMax)
        return M