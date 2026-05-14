class Solution:
    def maxA(self, n: int) -> int:
        if n <= 6:
            return n
        dp = [0] *  (n + 1)
        for v in range(n + 1):
            dp[v] = v
            for j in range(2, v - 3):
                dp[v] = max(dp[v], dp[v - j - 1] * j)
        
        return dp[n]

        # AAAAA
        # AAacv = AAAA
        # AAAacv = AAAAAA
        # AAAAAAA = A 8 7
        # AAAAacv = A x 8

        # [0,1,2,3,4,5,6,7]
        # [0,1,2,3,4,5,6, [-3=4]*2 = 4 * 2 OR [-4=3]*3]
        # Ctrl-A-C
        # Ctrl-V
