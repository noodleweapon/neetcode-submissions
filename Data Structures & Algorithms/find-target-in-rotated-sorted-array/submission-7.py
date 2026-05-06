class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # invariant: target is in [l, r] inclusive.

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                # now target can't be at m.
                if nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < target:
                if nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return m
        
        return -1