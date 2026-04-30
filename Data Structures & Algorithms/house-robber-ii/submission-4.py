class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        if len(nums) == 3:
            return max(nums)
        
        # mi = 0
        # mv = nums[0]
        # for i, v in enumerate(nums):
        #     if v > mv:
        #         mi = i
        #         mv = v
        
        M = 0
        for offset in [0, 1]:
            a = nums[0 + offset]
            b = max(a, nums[1 + offset])
            for i in range(2 + offset, len(nums) - 1 + offset):
                c = max(a + nums[i], b)
                a = b
                b = c
            M = max(b, M)
        return M