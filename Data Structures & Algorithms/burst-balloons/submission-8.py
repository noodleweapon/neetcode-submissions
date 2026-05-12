class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (N + 2) for _ in range(N + 2)] # R+1 by R+1

        # for i in range(1, N + 1):
        #     dp[i][i] = nums[i] # popped last
        
        for w in range(1, N + 1):
            for l in range(1, N + 2 - w):
                r = l + w - 1
                for i in range(l, r + 1):
                    left = dp[l][i - 1] if l <= i - 1 else 0
                    right = dp[i + 1][r] if i + 1 <= r else 0
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    dp[l][r] = max(dp[l][r], left + coins + right)

        return dp[1][N]
