class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        l = 0
        r = nums[0]
        jumps = 1
        while r < len(nums) - 1:
            jumps += 1
            for i in range(l, min(len(nums), r + 1)):
                new_r = i + nums[i]
                if new_r > r:
                    r = new_r
                    l = i
        return jumps