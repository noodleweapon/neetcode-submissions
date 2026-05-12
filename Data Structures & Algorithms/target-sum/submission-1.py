class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def rec(i, s):
            if i == len(nums):
                return 1 if s == 0 else 0
            return rec(i + 1, s + nums[i]) + rec(i + 1, s - nums[i])
        return rec(0, target)