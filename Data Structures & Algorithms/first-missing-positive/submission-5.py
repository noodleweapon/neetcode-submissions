class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != i + 1:
                j = nums[i] - 1
                if nums[j] == j + 1: # remote is already correctly placed.
                    break
                nums[i], nums[j] = nums[j], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

        # -2,-1,0
        # 1,2,-2,4,-1,5
        # return deadFrom - 1
        # 1,2,3,4,5,6,1