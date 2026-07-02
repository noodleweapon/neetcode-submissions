class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        v = None
        f = 0
        i = 0
        r = n - 1
        while i <= r:
            if nums[i] != v:
                v = nums[i]
                f = 1
            else:
                f += 1
            is_last_of_this_digit = i == r or nums[i + 1] != nums[i]
            if is_last_of_this_digit and f > 2:
                left_shift_by = f - 2
                for j in range(i, r + 1):
                    nums[j - left_shift_by] = nums[j]
                i -= left_shift_by
                r -= left_shift_by
            i += 1
        return r + 1