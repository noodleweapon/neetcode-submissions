class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(0, len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans