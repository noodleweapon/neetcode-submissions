class Solution:
    def rec(self, i, nums, target):
        if i == len(nums):
            return 1 if target == 0 else 0
        
        n = self.rec(i + 1, nums, target + nums[i])
        n += self.rec(i + 1, nums, target - nums[i])
        return n

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.rec(0, nums, target)