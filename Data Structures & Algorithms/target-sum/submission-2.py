class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def rec(i, s):
            if i == len(nums):
                return 1 if s == 0 else 0
            if (i, s) in dp:
                return dp[(i, s)]
            dp[(i, s)] = rec(i + 1, s + nums[i]) + rec(i + 1, s - nums[i])
            return dp[(i, s)]
        return rec(0, target)