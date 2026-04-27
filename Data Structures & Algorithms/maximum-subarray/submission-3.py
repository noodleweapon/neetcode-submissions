class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        # m = 0
        # s = float("-inf")

        # for r in range(len(nums)):
        #     if s < 0:
        #         s = nums[r]
        #     else:
        #         s += nums[r]
        #     m = max(m, s)
        # return s

        m = nums[0]
        s = 0
        for n in nums:
            s = max(0, s) + n
            m = max(s, m)
        return m