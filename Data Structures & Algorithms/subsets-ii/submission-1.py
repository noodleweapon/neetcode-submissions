class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        def rec(i, items):
            if i == len(nums):
                out.append(items.copy())
                return
            candidate = nums[i]
            j = i
            while j < len(nums) and candidate == nums[j]:
                j += 1
            
            rec(j, items)
            for _ in range(i, j):
                items.append(candidate)
                rec(j, items)

            for _ in range(i, j):
                items.pop()

        rec(0, [])
        return out
