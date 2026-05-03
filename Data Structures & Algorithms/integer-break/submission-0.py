class Solution:
    def integerBreak(self, n: int) -> int:
        original = n
        prod = 1
        while n >= 5:
            n -= 3
            prod *= 3
        if n == 4:
            return 4 * prod
        if n == 3:
            if original == 3:
                return 2
            else:
                return 3 * prod
        if n == 2:
            if original == 2:
                return 1
            else:
                return 2 * prod
        return prod


        # dp = [-1, -1, 1, 2, 4, 6, 9]
        # i = len(dp) - 1 # last index, represents count.
        # while n > i:
        #     M = max(dp[-3] * 3, dp[-2] * 2, dp[-1] * 1)
        #     dp.append(M)
        
        # return dp[n]

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



        
        #     1 + 2
        
        # if n == 4:
        #     WHY 3???
        



        # [1 = 1]




        # # 2 <= n <= 58

        # 3 x 3 x 3 x 3 
        # 4 + 4 + 4
        # 12

        # 2*2*2*2*2*2
        # 2 ^ 6 = 64

        # 1+1+1 smallest.