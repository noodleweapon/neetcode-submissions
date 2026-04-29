class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = None

        n = len(nums)
        for i, num in enumerate(nums):
            if num == 0 or num == None: # this means it was originally non positive
                continue
            num = abs(num) # if value <= 0 then seen.
            if num > n: # out of bounds, so we don't care
                continue
            if nums[num - 1] == None:
                nums[num - 1] = 0
            elif nums[num - 1] > 0:
                nums[num - 1] = -1 * nums[num - 1]
        
        for i, num in enumerate(nums):
            if num == None or num > 0:
                return i + 1
        return n + 1

# [1,2,0,0,4]