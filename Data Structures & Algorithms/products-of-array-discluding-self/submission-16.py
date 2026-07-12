class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        toLeft = [1] * n
        prod = 1
        for i in range(n):
            toLeft[i] = prod
            prod *= nums[i]
        
        prod = 1
        toRight = [1] * n
        for i in reversed(range(n)):
            toRight[i] = prod
            prod *= nums[i]
        
        return [toLeft[i] * toRight[i] for i in range(n)]
