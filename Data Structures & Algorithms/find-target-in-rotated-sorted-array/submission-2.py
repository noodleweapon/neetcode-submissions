class Solution:
    def get_offset(self, nums):
        l, r = 0, len(nums) - 1
        minv = float('inf')
        mini = 0
        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < minv:
                    minv = nums[l]
                    mini = l
                break
            m = (l + r) // 2
            if nums[m] < minv:
                minv = nums[m]
                mini = m
            left_sorted = nums[l] <= nums[m]
            if left_sorted:
                l = m + 1
            else:
                r = m - 1
        return mini

    def search(self, nums: List[int], target: int) -> int:
        offset = self.get_offset(nums)
        print(offset)

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            ind = (m + offset) % len(nums)
            if target == nums[ind]:
                return ind
            elif target < nums[ind]:
                r = m - 1
            else:
                l = m + 1
        return -1

