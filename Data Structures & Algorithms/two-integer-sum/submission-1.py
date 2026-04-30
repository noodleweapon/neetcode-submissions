class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j in range(i, len(nums)):
                b = nums[j]
                s = a + b
                if s == target:
                    return [i, j]
        