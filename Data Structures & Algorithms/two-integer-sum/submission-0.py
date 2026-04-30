class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:]):
                s = a + b
                if s == target:
                    return [i, j]
        