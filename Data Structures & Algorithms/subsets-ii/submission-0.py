import copy
class Solution:
    def rec(self, i, cur, res, nums):
        if i >= len(nums):
            res.append(copy.deepcopy(cur))
            return


        cur.append(nums[i])
        self.rec(i + 1, cur, res, nums)
        cur.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.rec(i + 1, cur, res, nums)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []
        nums.sort()
        self.rec(0, cur, res, nums)
        return res