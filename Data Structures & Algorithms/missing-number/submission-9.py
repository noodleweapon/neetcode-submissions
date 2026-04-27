class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        v = 0
        for i in range(len(nums) + 1):
            v ^= i
        for num in nums:
            v ^= num
        return v


        # Naive approach
        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         return i