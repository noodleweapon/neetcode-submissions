class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        dp = [0] * n
        def dpGet(i):
            if i >= n:
                return 0
            return dp[i]

        def stoneSum(i, count):
            end = min(n, i+count)
            return sum(stones[i:end])

        for i in reversed(range(n)):
            dp[i] = max([
                stoneSum(i, 1) - dpGet(i + 1),
                stoneSum(i, 2) - dpGet(i + 2),
                stoneSum(i, 3) - dpGet(i + 3)
            ])
        final = dp[0]
        if final > 0:
            return 'Alice'
        elif final < 0:
            return 'Bob'
        else:
            return 'Tie'