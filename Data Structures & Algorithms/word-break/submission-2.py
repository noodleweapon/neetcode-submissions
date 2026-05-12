class Solution:
    def rec(self, n, s, words, dp) -> bool:
        if n == len(s):
            return True
        if dp[n] != -1:
            return dp[n]
        for word in words:
            if n + len(word) > len(s):
                continue
            if s[n:n + len(word)] != word:
                continue
            if self.rec(n + len(word), s, words, dp):
                dp[n] = True
                return True
        dp[n] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * len(s)
        return self.rec(0, s, wordDict, dp)