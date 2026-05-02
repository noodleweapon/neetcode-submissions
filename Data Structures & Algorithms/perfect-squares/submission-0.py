class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        z = 0
        while True:
            z += 1
            x = z * z
            if x > n:
                break
            elif x == n:
                return 1
            else:
                squares.append(x)
        
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for square in reversed(squares):
            for j in range(1, n + 1):
                if j < square:
                    continue
                dp[j] = min(dp[j], dp[j - square] + 1)
        return dp[n]

        
        # 012345678
        # 01121.  2
