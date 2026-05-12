class Solution:
    def productExceptSelfSlow(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                res[i] *= nums[j]
        return res


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls = []
        p = 1
        for num in nums:
            p *= num
            ls.append(p)

        rs = []
        q = 1
        for num in list(reversed(nums)):
            q *= num
            rs.append(q)
        
        res = []
        for i, num in enumerate(nums):
            l_ind = i - 1
            r_ind = len(nums) - i - 2
            L = 1 if l_ind < 0 else ls[l_ind]
            R = 1 if r_ind < 0 else rs[r_ind]
            res.append(L*R)
        return res