class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        
        maxI = 0
        for i in range(len(nums)):
            if i > maxI:
                return False
            maxI = max(maxI, i + nums[i])
        return maxI >= len(nums) - 1