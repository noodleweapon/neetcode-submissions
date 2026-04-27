class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t = sum(nums)
        if t == 0:
            return 0

        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s == t - s + nums[i]:
                return i
        return -1
