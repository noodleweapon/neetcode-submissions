class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if all(nums[i] >= nums[i + 1] for i in range(n - 1)):
            nums.reverse()
            return
        
        for i in reversed(range(n - 1)):
            if nums[i] < nums[i + 1]:
                greater = min([x for x in nums[i+1:] if x > nums[i]])
                for ind in reversed(range(i + 1, n)):
                    if nums[ind] == greater:
                        break

                nums[i], nums[ind] = nums[ind], nums[i]
                nums[i+1:n] = reversed(nums[i+1:n])
                break
        
        # 2,1,3,2


        # 3,4,5,2
        # 3,2,4,5
        # 3,5,2,4

        