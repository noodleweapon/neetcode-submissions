class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def rec(l, r): # l, r excluded
            if l == r - 1:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            M = 0
            for i in range(l + 1, r):
                z = nums[l] * nums[i] * nums[r]
                z += rec(l, i) + rec(i, r)
                M = max(z, M)
            dp[(l, r)] = M
            return M

        
        return rec(0, len(nums) - 1)