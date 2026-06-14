class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            if i % 2:
                if nums[i - 1] <= nums[i]:
                    continue
            else:
                if nums[i - 1] >= nums[i]:
                    continue
                
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
