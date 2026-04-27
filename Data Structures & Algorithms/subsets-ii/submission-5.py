class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        def rec(i, items):
            out.append(items.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                items.append(nums[j])
                rec(j + 1, items)
                items.pop()
        rec(0, [])
        return out