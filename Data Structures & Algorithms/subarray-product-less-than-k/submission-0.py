class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        p = 1
        res = 0
        for r in range(n):
            p *= nums[r]
            while p >= k and l < r:
                p /= nums[l]
                l += 1
            if p < k:
                res += r - l + 1
        return res
