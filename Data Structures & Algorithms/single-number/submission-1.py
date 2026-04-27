class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for v in nums:
            n = n ^ v
        return n