class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        def rec(i, t):
            if i == len(nums):
                return False
            if 2 * t == s:
                return True
            return rec(i + 1, t + nums[i]) or rec(i + 1, t)
            
        return rec(0, 0)