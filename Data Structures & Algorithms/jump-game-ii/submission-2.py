# [7,0,9,6,9,6,1,7.  ,9,0,1,2.   ,9,0,3]

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        l = r = 0
        maxR = 0
        jumps = 0
        while maxR < len(nums) - 1:
            r = maxR
            while l <= r:
                maxR = max(nums[l] + l, maxR)
                l += 1
            jumps += 1
            
        return jumps
        # m = 0
        # n = 0
        # for i, num in enumerate(nums):
        #     if i + num > m:
        #         n += 1
        #         m = i + num
        #     if m >= len(nums) - 1:
        #         break
        # return n

