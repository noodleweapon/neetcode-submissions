class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        out = []
        def rec(i, items):
            if i == len(nums):
                out.append(items.copy())
                return
            for j, num in enumerate(nums):
                if j in seen:
                    continue
                seen.add(j)
                items.append(nums[j])
                rec(i + 1, items)
                items.pop()
                seen.remove(j)
        rec(0, [])
        return out