class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        m = nums[0]
        s = 0
        for n in nums:
            s = max(0, s) + n
            m = max(s, m)
        return m