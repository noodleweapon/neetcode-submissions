class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(items):
            x = 0
            for item in items:
                x ^= item
            return x

        def rec(i, items):
            if i == len(nums):
                return xor(items)
            tot = 0
            items.append(nums[i])
            tot += rec(i + 1, items)
            items.pop()
            tot += rec(i + 1, items)
            return tot

        return rec(0, [])