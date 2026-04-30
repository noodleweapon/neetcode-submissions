class Solution:
    def rec(self, s, i, twoDigits, dp):
        if i < 0:
            return 0
        if dp[twoDigits][i] != -1:
            return dp[twoDigits][i]
        if i == 0:
            return 0 if s[i] == "0" else 1
        digits = int(s[i] + s[i - 1] if twoDigits else s[i])
        if not (1 <= int(s[i]) <= 26):
            dp[twoDigits][i] = 0
            return 0
        
        res = self.rec(s, i - 1, False, dp) + self.rec(s, i - 2, True, dp)
        dp[twoDigits][i] = res
        return res

    def numDecodings(self, s: str) -> int:
        dp = {k: [-1] * (len(s)) for k in [True, False]}
        return self.rec(s, len(s) - 2, True, dp) + self.rec(s, len(s) - 1, False, dp)

        
            
            # if s[0] == "0":
            #     return 0
            # n = 0
            # i = len(s)
            # while i >= 0:
            #     i -= 1
            #     if (1 <= int(s[i]) <= 26):
            #         n += 1
                
            #     if i == 0:
            #         break
            #     if (1 <= int(s[i] + s[i - 1]) <= 26):
            #         n += 1
            # return n