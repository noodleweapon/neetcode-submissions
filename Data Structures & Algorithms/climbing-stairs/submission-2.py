class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(k):
            if k < 0:
                return 0
            if k == 0:
                return 1
            return rec(k - 1) + rec(k - 2)
        
        return rec(n)