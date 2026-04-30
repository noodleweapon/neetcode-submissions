class Solution:
    def get_offset(self, nums, target):
        if nums[0] < nums[-1]:
            return 0

        l = 0
        r = len(nums) - 1
        while l < r:
            if r - l == 1:
                return l + 1
            m = l + ((r - l) // 2)
            L = nums[l]
            R = nums[r]
            M = nums[m]

            if L > R:
                if M > L:
                    l = m
                elif M < R:
                    r = m
        return m + 1

    def ind(self, nums, offset, i):
        return (i + offset) % len(nums)

    def get_ind(self, nums, target, offset):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            M = nums[self.ind(nums, offset, m)]
            if M == target:
                return self.ind(nums, offset, m)
            elif target < M:
                r = m - 1
            elif target > M:
                l = m + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        off = self.get_offset(nums, target)
        print(off)
        return self.get_ind(nums, target, off)
