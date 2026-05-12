class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        nums.sort()
        res = 0
        
        for i in range(n):
            if nums[i] * 2 > target:
                break
            L = nums[i]
            l, r = i, n - 1
            
            while l < r:
                m = (l + r + 1) // 2
                if L + nums[m] <= target:
                    l = m
                else:
                    r = m - 1
            res += pow(2, l - i, mod)
            res %= mod
        return res