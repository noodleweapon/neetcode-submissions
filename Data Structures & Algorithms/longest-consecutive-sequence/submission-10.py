class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        ans = 0
        for n in nums[1:]:
            inc = n - prev
            if inc > 1:
                break
            else:
                ans += 1
                prev += inc
        return ans