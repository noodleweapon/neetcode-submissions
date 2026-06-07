class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = 0
        t = 0
        res = float("inf")
        for r in range(len(nums)):
            t += nums[r]
            if t < target:
                continue
            while l < r and t - nums[l] >= target:
                t -= nums[l]
                l += 1
            res = min(res, r - l + 1)
        if res == float("inf"):
            return 0
        return res

        # 2,1,5,1,5,3
        # target = 10
