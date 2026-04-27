# needs to be more efficient
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s // 2
        memo = {}

        def rec(i, t):
            if i == len(nums):
                return False
            if (t, i) in memo:
                return memo[(t, i)]
            if t == s:
                return True
            memo[(t, i)] = rec(i + 1, t + nums[i]) or rec(i + 1, t)
            return memo[(t, i)]
            
        return rec(0, 0)