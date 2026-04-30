class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls = []
        p = 1
        for num in nums[:-1]:
            p *= num
            ls.append(p)

        rs = []
        q = 1
        for num in list(reversed(nums[1:])):
            q *= num
            rs.append(q)
        
        res = []
        for i, num in enumerate(nums):
            l_ind = i - 1
            r_ind = len(nums) - i - 1
            L = 1 if l_ind < 0 else nums[l_ind]
            R = 1 if r_ind < 0 else nums[r_ind]
            res.append(L*R)
        return res