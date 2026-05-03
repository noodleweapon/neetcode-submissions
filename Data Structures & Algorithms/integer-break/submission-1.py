class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [-1, -1, 1, 2, 4, 6, 9]
        i = len(dp) - 1 # last index, represents count.
        while n > i:
            i += 1
            M = max(dp[i - 3] * 3, dp[i - 2] * 2, dp[i - 1] * 1)
            dp.append(M)
        
        return dp[n]

        # n == 0
        # n == 1
        # if n == 2: # 2 = 1 + 1, 1*1 = 1
        #     return 1
        # if n == 3: # 3 = 1 + 2, 1*2 = 2
        #     return 2
        # if n == 4: # 4 = 2 + 2, 2*2 = 4
        #     return 4
        # if n == 5: # 5 = 2 + 3, 2*3 = 6
        #     return 6
        # if n == 6: # 6 = 3 + 3, 3*3 = 9
        #     return 9
        # n == 7: # 7 = (6 --> 9) * 1 = 9
        #           OR. (5 --> 6) * 2 = 12
        #           OR  (4 --> 4) * 3 = 12

        # 7 = 3 * 2*2 = 12



