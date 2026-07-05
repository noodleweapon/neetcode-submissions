class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n // 2
        while l < r:
            m = (l + r - 1) // 2
            cond = (m == n - 1) or (nums[m * 2] != nums[m * 2 + 1])
            if cond:
                r = m
            else:
                l = m + 1
        return nums[l * 2]