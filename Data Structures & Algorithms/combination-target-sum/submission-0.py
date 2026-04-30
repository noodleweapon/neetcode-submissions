import copy

class Solution:
    def rec(self, i, cur, nums, res, target):
        if target == 0:
            res.append(copy.deepcopy(cur))
            return
        
        if i >= len(nums):
            return
        if nums[i] > target:
            return

        cur.append(nums[i])
        self.rec(i, cur, nums, res, target - nums[i])
        cur.pop()

        self.rec(i + 1, cur, nums, res, target)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        uniq = []
        for num in nums:
            if num in uniq:
                continue
            uniq.append(num)

        res, cur = [], []
        self.rec(0, cur, uniq, res, target)
        return res
