class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        R = []
        p = 1
        for num in reversed(nums[1:]):
            p *= num
            R.append(p)
        L = []
        p = 1
        for num in nums[:-1]:
            p *= num
            L.append(p)

        res = []
        for i in range(nums):
            ans = 1
            if i != 0:
                ans *= L[i - 1]
            if i != len(nums) - 1:
                ans *= R[len(nums) - 2 + i]
            res.append(ans)
        
        return res