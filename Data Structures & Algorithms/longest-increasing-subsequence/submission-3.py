class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        for i in reversed(range(len(nums))):
            M = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    M = max(M, 1 + dp[j])
            dp[i] = M
        return max(dp)