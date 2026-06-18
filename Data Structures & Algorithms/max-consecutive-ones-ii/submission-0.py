class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        flipped = 0
        M = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flipped += 1
                while flipped > 1 and l < r:
                    if nums[l] == 0:
                        flipped -= 1
                    l += 1
            M = max(M, r - l + 1)
        return M