class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def rec(i, subset):
            res.append(subset.copy())

            for j in range(i, len(nums)):
                if j > i and nums[i] == nums[j]:
                    continue
                
                subset.append(nums[i])
                rec(j + 1, subset)
                subset.pop()
        rec(0, [])
        return res