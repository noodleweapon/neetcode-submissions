class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1 # invariant
        while l < r:
            m = (l + r) // 2
            cond = nums[m] > nums[r]
            if cond:
                l = m + 1
            else:
                r = m
        return nums[l]

        # [3,4,5,6,1,2]