class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = nums[0]
        for l, num in enumerate(nums):
            if l > r:
                return False
            new_r = l + nums[l]
            r = max(r, new_r)
        return True