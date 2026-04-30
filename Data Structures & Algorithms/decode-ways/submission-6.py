class Solution:
    def rec(self, s, i, twoDigits, dp):
        if i < 0:
            return 0
        if dp[twoDigits][i] != -1:
            return dp[twoDigits][i]
        
        digits = int(s[i] + s[i - 1] if twoDigits else s[i])

        if (not (1 <= digits <= 26)) or (s[i] == "0"):
            dp[twoDigits][i] = 0
            return 0
        if i == 0:
            return 1
        
        res = self.rec(s, i - 1, False, dp) + self.rec(s, i - 2, True, dp)
        dp[twoDigits][i] = res
        return res

    def numDecodings(self, s: str) -> int:
        dp = {k: [-1] * (len(s)) for k in [True, False]}
        return self.rec(s, len(s) - 2, True, dp) + self.rec(s, len(s) - 1, False, dp)