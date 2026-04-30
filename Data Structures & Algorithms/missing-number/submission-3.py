class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            v = i ^ nums[i]
            if v != 0:
                return i
        return 0