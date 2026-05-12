import copy
class Solution:
    def rec(self, i, curr, res, nums):
        if i >= len(nums):
            res.append(copy.deepcopy(curr))
            return
        
        self.rec(i + 1, curr, res, nums)
        curr.append(nums[i])
        self.rec(i + 1, curr, res, nums)
        curr.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        self.rec(0, curr, res, nums)
        return res