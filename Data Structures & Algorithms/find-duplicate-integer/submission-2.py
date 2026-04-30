class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        M = max(nums)
        num_dups = N - M
        print(num_dups)
        unique_sum = (M * (M + 1)) // 2
        excess_sum = sum(nums) - unique_sum
        return excess_sum // num_dups