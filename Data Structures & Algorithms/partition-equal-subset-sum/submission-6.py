class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s // 2
        
        memo = [False] * (s + 1)
        memo[0] = True

        for num in nums:
            for v in reversed(range(s + 1)):
                if v < num:
                    continue
                if memo[v - num]:
                    memo[v] = True

        return memo[s]