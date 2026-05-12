class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def rec(i, xor):
            if i == len(nums):
                return xor
            tot = 0
            tot += rec(i + 1, xor ^ nums[i])
            tot += rec(i + 1, xor)
            return tot

        return rec(0, 0)