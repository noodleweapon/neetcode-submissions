class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        seen = [False] * len(nums)

        def rec(items, seen):
            if len(items) == len(nums):
                out.append(items.copy())
                return
            for i, num in enumerate(nums):
                if seen[i]:
                    continue
                seen[i] = True
                items.append(num)
                rec(items, seen)
                items.pop()
                seen[i] = False

        rec([], seen)
        return out
