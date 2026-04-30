class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        def rec(i, subset):
            out.append(subset.copy())
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[i]:
                    continue
                subset.append(nums[j])
                rec(j + 1, subset)
                subset.pop()
        
        rec(0, [])
        return out