class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        def ways(d):
            return d * (d + 1) // 2
        res = 0
        length = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                length += 1
            else:
                res += ways(length)
                length = 1
        if length > 0:
            res += ways(length)
        return res
        
        # 1,3,5,4,4,6
        # 2 --> 2 + 1 = 3 = 2 * (2 + 1) / 2 = 3
        # 3 --> 3 + 2 + 1 = 6, 3 * (3 + 1) / 2 = 6
