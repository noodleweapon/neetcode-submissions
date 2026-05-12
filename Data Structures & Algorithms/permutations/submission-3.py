class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def rec(items):
            if len(items) == len(nums):
                out.append(items.copy())
                return
            for num in nums:
                if num in items:
                    continue
                items.append(num)
                rec(items)
                items.pop()

        rec([])
        return out
