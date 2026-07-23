class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        res = 0
        for num in nums:
            u = num
            while u in S:
                u += 1
            res = max(res, u - num)
        return res