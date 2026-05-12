class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        
        inits = []
        for z in reversed(range(1, k + 1)):
            inits.append(nums[len(nums) - z])
        
        for i in reversed(range(len(nums))):
            if i < k:
                nums[i] = inits[i]
            else:
                nums[i] = nums[(i + n - k) % n]



        # for _ in range(k):
        #     temp = nums[len(nums) - 1]
        #     for i in reversed(range(len(nums))):
        #         if i == 0:
        #             nums[i] = temp
        #         else:
        #             nums[i] = nums[(i + n - 1) % n]


        
        # allocate an arr length k.
        # [1,2,3,4,5,6,7,8]
        # [5,6,7,8,1,2,3,4]