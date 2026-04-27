class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def rec(i, subset):
            if i == len(nums):
                out.append(subset.copy())
                return
            rec(i + 1, subset)
            subset.append(nums[i])
            rec(i + 1, subset)
            subset.pop()
        rec(0, [])
        return out