class Solution:
    def sub(self, nums):
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            c = max(a + nums[i], b)
            a, b = b, c
        return b

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[1]
        a = nums[1:]
        b = nums[:-1]
        return max(self.sub(a), self.sub(b))