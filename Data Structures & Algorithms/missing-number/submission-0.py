class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        s = l * (l + 1) // 2
        return s - sum(nums)