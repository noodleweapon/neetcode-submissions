class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # invariant: target is in [l, r] inclusive.

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: # left sorted
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else: # right sorted
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1