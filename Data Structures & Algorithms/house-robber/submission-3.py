class Solution:

    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
        
    #     left = nums[0]
    #     right = nums[1]
    #     while right < len(nums):
            

    def rec(self, nums: List[int], i, dp) -> int:
        if i < 0:
            return 0
        if i in dp:
            return dp[i]
        s = max(self.rec(nums, i - 3, dp), self.rec(nums, i - 2, dp))
        res = s + nums[i]
        dp[i] = res
        return res

    def rob(self, nums: List[int]) -> int:
        dp = {}
        si = len(nums) - 1
        return max(self.rec(nums, si, dp), self.rec(nums, si - 1, dp))