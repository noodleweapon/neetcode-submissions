class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxsum = nums[0]
        
        for i, num in enumerate(nums):
            if i > maxsum:
                return False
            maxsum = max(i + num, maxsum)
        return maxsum >= len(nums)
