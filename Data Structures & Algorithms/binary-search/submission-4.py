class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            k = (i + j) // 2
            m = nums[k]
            if m == target:
                return k
            elif m < target:
                i = k + 1
            else:
                j = k - 1
        return -1