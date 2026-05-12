class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2
            missing = (nums[m] - nums[0]) - (m - 0)
            cond = missing >= k
            if cond:
                r = m
            else:
                l = m + 1

        missing = (nums[l] - nums[0]) - (l - 0)
        if missing < k:
            return nums[l] + (k - missing)
        else:
            return nums[l] - (1 + missing - k)


