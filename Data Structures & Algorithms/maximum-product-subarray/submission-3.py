class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        least = most = nums[0]
        res = least
        for i in range(1, len(nums)):
            num = nums[i]
            least, most = min(least * num, most * num, num), max(least * num, most * num, num)
            res = max(res, most)
        return res