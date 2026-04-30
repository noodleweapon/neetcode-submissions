class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        M = max(nums)
        v = 0
        for i in range(len(nums)):
            v = v ^ i
            if nums[i] != M:
                v = v ^ nums[i]
        return v


        # Naive approach
        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         return i