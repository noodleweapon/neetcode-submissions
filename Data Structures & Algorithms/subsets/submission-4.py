class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def rec(i, subset):
            if i == len(nums):
                out.append(subset)
                return
            subset.append(nums[i])
            rec(i + 1, subset)
            subset.pop()
            rec(i + 1, subset)
        
        rec(0, [])
        return out