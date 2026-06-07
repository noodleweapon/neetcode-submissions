class Solution:
    def findMin(self, nums: List[int]) -> int:
        [3,4,5,6,1,2]
        [1,2,3,4,5,6]

        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            cond = nums[m] < nums[r]
            if not cond:
                l = m + 1
            else:
                r = m

        return nums[l]