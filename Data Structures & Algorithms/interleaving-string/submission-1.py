class Solution:
    def rec(self, Z, X, Y, zi, xi, yi, dp):
        if zi >= len(Z):
            return True
        if dp[yi][xi] != -1:
            return dp[yi][xi]

        if xi < len(X) and X[xi] == Z[zi]:
            if self.rec(Z, X, Y, zi + 1, xi + 1, yi, dp):
                dp[yi][xi] = True
                return True
        
        if yi < len(Y) and Y[yi] == Z[zi]:
            if self.rec(Z, X, Y, zi + 1, xi, yi + 1, dp):
                dp[yi][xi] = True
                return True
        
        dp[yi][xi] = False
        return False

    def isInterleave(self, X: str, Y: str, Z: str) -> bool:
        dp = [[-1] * (1 + len(X)) for _ in range(1 + len(Y))]
        return self.rec(Z, X, Y, 0, 0, 0, dp)
        