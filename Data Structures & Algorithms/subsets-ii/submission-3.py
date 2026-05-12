class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        def rec(level, items):
            out.append(items.copy())
            for j in range(level, len(nums)):
                if j > level and nums[j] == nums[j - 1]:
                    continue
                items.append(nums[j])
                rec(j + 1, items)
                items.pop()
            
        rec(0, [])
        return out

        # [1, 1, 2]
        # level = 0
        # j = [1, 2]
        # [1, 1]

        # [2]