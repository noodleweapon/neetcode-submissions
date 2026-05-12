class Solution:
    def rec(self, i, cap, nums):
        if i == len(nums):
            return cap == 0
        
        if self.rec(i + 1, cap, nums):
            return True

        if nums[i] <= cap:
            if self.rec(i + 1, cap - nums[i], nums):
                return True

        return False

    def canPartition(self, nums: List[int]) -> bool:
        cap = sum(nums)
        if cap % 2 == 1:
            return False

        return self.rec(0, cap // 2, nums)