class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n): # With i'th one as the min.
            if nums[i] * 2 > target:
                break
            l, r = i, n - 1
            while l < r:
                m = (l + r + 1) // 2
                # cond = find the biggest index such that min + max <= target.
                if nums[i] + nums[m] <= target:
                    l = m
                else:
                    r = m - 1
            res += 2 ** (l - i)
            res %= MOD
        return res % MOD