# Bob should minimize Alice’s future total, not “Alice minus Bob’s stones”.
# BAD:
# val = rec(i + X, max(M, X), not alice)
# minimize = -sum(piles[i:i+X]) + val
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        def rec(i, M, alice):
            if i >= n:
                return 0
            if (i, M, alice) in dp:
                return dp[(i, M, alice)]
            if alice:
                res = float("-inf")
                for X in range(1, 2 * M + 1):
                    res = max(res, sum(piles[i:i+X]) + rec(i + X, max(M, X), not alice))
            else:
                res = float("inf")
                for X in range(1, 2 * M + 1):
                    res = min(res, rec(i + X, max(M, X), not alice))
            dp[(i, M, alice)] = res
            return res

        return rec(0, 1, True)

        # [3,1,2,5,7]
        # 1 <= x <= 2M

