class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = [False] * len(nums)
        out = []
        def rec(i, items):
            if i == len(nums):
                out.append(items.copy())
                return
            for j, num in enumerate(nums):
                if seen[j]:
                    continue
                seen[j] = True
                items.append(nums[j])
                rec(i + 1, items)
                items.pop()
                seen[j] = False
        rec(0, [])
        return out