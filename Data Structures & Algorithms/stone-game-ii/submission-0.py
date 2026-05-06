class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        def dfs(alice, i, M):
            if i == n:
                return 0
            key = (alice, i, M)

            res = 0 if alice else float("inf")
            pref = 0
            for X in range(1, 2 * M + 1):
                if i + X - 1 == n:
                    break
                pref += piles[i + X - 1]

                if alice:
                    res = max(res, pref + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))

            return res
        
        return dfs(True, 0, 1)