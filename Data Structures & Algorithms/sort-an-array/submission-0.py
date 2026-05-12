class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for j in range(n):
            i = j - 1
            while i >= 0 and nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i -= 1
        return nums