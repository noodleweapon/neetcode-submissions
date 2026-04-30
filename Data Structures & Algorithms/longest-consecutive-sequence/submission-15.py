class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        prev = nums[0]
        ans = 1
        for n in nums[1:]:
            inc = n - prev
            if inc == 0:
                continue
            if inc > 1:
                break
            else:
                ans += 1
                prev += 1
        return ans