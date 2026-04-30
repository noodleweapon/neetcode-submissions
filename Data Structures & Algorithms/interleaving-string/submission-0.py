class Solution:
    def rec(self, Z, X, Y, zi, xi, yi):
        if zi >= len(Z):
            return True

        if xi < len(X) and X[xi] == Z[zi]:
            if self.rec(Z, X, Y, zi + 1, xi + 1, yi):
                return True
        
        if yi < len(Y) and Y[yi] == Z[zi]:
            if self.rec(Z, X, Y, zi + 1, xi, yi + 1):
                return True
        
        return False

    def isInterleave(self, X: str, Y: str, Z: str) -> bool:
        return self.rec(Z, X, Y, 0, 0, 0)
        