class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = [1] * len(nums)
    #     for i, num in enumerate(nums):
    #         for j in range(len(nums)):
    #             if i == j:
    #                 continue
    #             res[j] *= num
    #     return res
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []
        p = 1
        for num in nums[:-1]:
            p *= num
            L.append(p)

        R = []
        p = 1
        for num in reversed(nums[1:]):
            p *= num
            R.append(p)

        res = []
        for i in range(len(nums)):
            ans = 1
            if i != 0:
                ans *= L[i - 1]
            
            # i = len(nums) - 1:
            #     No right;
            
            # i = len(nums) - 2:
            #     R[0]
            
            # i = 0:
            #     R[len(nums) - 2]
            
            if i != len(nums) - 1:
                ans *= R[len(nums) - 2 - i]

            res.append(ans)
        
        return res