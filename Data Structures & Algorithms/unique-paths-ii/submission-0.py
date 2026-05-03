class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        R = len(g)
        C = len(g[0])
        dp = [[0] * C for _ in range(R)]
        #
        for c in range(C):
            if g[0][c] == 1:
                break
            dp[0][c] = 1
        
        for r in range(R):
            if g[r][0] == 1:
                break
            dp[r][0] = 1
        #
        for r in range(1, R):
            for c in range(1, C):
                if g[r][c] == 1:
                    continue
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[R - 1][C - 1]


        [0,0,1,0,0,0],

        [0,A,0],
        [B,X,1],
        [0,1,0]

        [0,1,0],
        [0,1,1],
        [0,0,0]