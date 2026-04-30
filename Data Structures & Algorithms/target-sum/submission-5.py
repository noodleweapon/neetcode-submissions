class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for i in range(len(nums)):
            nxt = defaultdict(int)
            for s, f in dp.items():
                nxt[s + nums[i]] = f + dp.get(s + nums[i], 0)
                nxt[s - nums[i]] = f + dp.get(s - nums[i], 0)
            dp = nxt
        return dp[target]