class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        for i in range(len(nums)):
            n = n ^ i
            n = n ^ nums[i]
        if n >= len(nums):
            return 0
        return n