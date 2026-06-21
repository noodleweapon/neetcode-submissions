class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        # 2 --> 1 ways.
        # 4 --> 2 ways (2 handshakes, minus that: 0)
        # numPeople = 6 --> 5 ways (3 handshakes. Minus that: 2)
        MOD = 10 ** 9 + 7
        dp = {}
        def numWays(ppl):
            if ppl in [0, 2]:
                return 1
            if ppl in dp:
                return dp[ppl]
            ways = 0
            for i in range(2, ppl + 1, 2):
                waysLeft = numWays(i - 2)
                waysRight = numWays(ppl - i)
                ways += waysLeft * waysRight
            dp[ppl] = ways
            return ways % MOD

        return numWays(numPeople)