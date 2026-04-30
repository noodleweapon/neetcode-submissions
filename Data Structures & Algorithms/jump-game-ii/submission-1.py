class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        m = 0
        n = 0
        for i, num in enumerate(nums):
            if i + num > m:
                n += 1
                m = i + num
            if m >= len(nums) - 1:
                break
        return n

