class Solution:
    def new21Game(self, upperLimit: int, drawIfLessThan: int, maxGain: int) -> float:
        if drawIfLessThan == 0:
            return 1
        dp = [0] * (upperLimit + 1)
        dp[0] = 1
        accum = 1
        for u in range(1, upperLimit + 1):
            remove = u - maxGain - 1
            if 0 <= remove < drawIfLessThan:
                accum -= dp[remove]
            dp[u] = accum / maxGain
            if u < drawIfLessThan:
                accum += dp[u]
        return sum(dp[drawIfLessThan:])






        
        # if False: # MISTAKE: Too slow. use sliding window.
        #     if drawIfLessThan == 0:
        #         return 1
        #     dp = [0] * (upperLimit + 1)
        #     dp[0] = 1
        #     for u in range(1, upperLimit + 1):
        #         lower = max(0, u - maxGain)
        #         upper = min(drawIfLessThan - 1, u - 1)
        #         for v in range(lower, upper + 1):
        #             dp[u] += dp[v] / maxGain
        #     return sum(dp[drawIfLessThan:])
        # # score = (0 --> + [1, maxPts] while pts < k)
        # # Pr(score <= upperLimit)
        # # Input: n = 6, k = 1, maxPts = 10