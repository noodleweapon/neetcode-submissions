class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        def rec(l, r): # l is included, r is excluded
            v = 0
            for m in range(l, r):
                p = nums[l - 1] * nums[m] * nums[r]
                z = rec(l, m) + rec(m + 1, r) + p
                v = max(v, z)
            return v
        return rec(1, n - 1)