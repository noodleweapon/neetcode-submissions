class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        r = nums[0]
        improving = True
        while improving:
            improving = False
            for i in range(l, max(len(nums), r + 1)):
                new_r = i + nums[i]
                if new_r > r:
                    r = new_r
                    l = i
                    improving = True
    
        return r >= len(nums) - 1