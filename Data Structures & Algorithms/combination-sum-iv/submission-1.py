class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        # nums.sort(reverse=True)
        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]


        # 3,1,2
        # 3,2,1

        #  0 1 2 3 4
        # [1,0,0,0,0]
        #    1 1 1 1
        #      2 2 3
        #        3 4

        #        1
        #      1   1
        #    1 2 3 3