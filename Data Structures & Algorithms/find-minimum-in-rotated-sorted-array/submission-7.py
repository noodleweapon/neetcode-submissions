class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        i = 1
        j = len(nums) - 1
        while i <= j:
            k = (i + j) // 2
            if nums[k - 1] > nums[k]:
                return nums[k]

            if nums[i] < nums[k - 1]:
                i = k
            elif nums[k] < nums[j]:
                j = k

        return -1
