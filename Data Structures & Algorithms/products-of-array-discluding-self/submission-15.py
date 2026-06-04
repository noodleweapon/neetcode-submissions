class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # -1,0,1,2,3
        # pref: [1, nums[0], nums[0] * nums[1], etc...]
        # postf: [nums[-1] * nums[-2], nums[-1], 1]

        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        p = q = 1
        for i in range(n - 1):
            p *= nums[i]
            prefix[i + 1] = p
            q *= nums[n - i - 1]
            postfix[n - i - 2] = q
        
        return [prefix[i] * postfix[i] for i in range(n)]