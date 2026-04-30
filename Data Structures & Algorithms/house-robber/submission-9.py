class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        i = 2
        a = nums[0]
        b = nums[1]
        while i <= len(nums):
            bNext = max(nums[i] + a, b)
            a, b = b, bNext
            i += 1
        return max(a, b)

    def rec(self, nums: List[int], i, dp) -> int:
        if i < 0:
            return 0
        if i in dp:
            return dp[i]
        res = max(self.rec(nums, i - 1, dp), self.rec(nums, i - 2, dp) + nums[i])
        dp[i] = res
        return res

    def robOld(self, nums: List[int]) -> int:
        dp = {}
        si = len(nums) - 1
        return self.rec(nums, si, dp)