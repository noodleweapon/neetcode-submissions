class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        bestL = 0
        while l <= r:
            print(l, r)
            m = (l + r) // 2
            if m * m > x:
                r = m - 1
            else:
                bestL = m
                print("bestL")
                print(bestL)
                l = m + 1
        return bestL