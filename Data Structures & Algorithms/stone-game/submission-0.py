class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # alice advantage
        # dp[i][j] is advantage for [i:j+1]
        # for person that goes first (alice)
        dp = [[None] * n for _ in range(n)]

        # advantage is person that goes first for 2 piles.
        for i in range(n - 1):
            j = i + 1
            dp[i][j] = abs(piles[i] - piles[j])
        
        # add to end of each, expand.
        # k is current width of dp.
        # goes from 2 to (n-1), makes sense.
        for k in range(2, n):
            for i in range(n - k):
                j = i + k
                a = piles[i] - dp[i + 1][j]
                b = piles[j] - dp[i][j - 1]
                dp[i][j] = max(a, b)
        
        return dp[0][n - 1] > 0

        
        # 5,20,3,2

        # 1,2,10,1,10,10

        
        # Alice: 1
        # Bob: 2
        # Alice: 3
        # Bob: 1
