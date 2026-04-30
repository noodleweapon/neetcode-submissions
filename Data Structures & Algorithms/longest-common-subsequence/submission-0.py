class Solution:
    def rec(self, s1, s2, i1, i2):
        if i1 == len(s1) or i2 == len(s2):
            return 0
        if s1[i1] == s2[i2]:
            return 1 + self.rec(s1, s2, i1 + 1, i2 + 1)
        else:
            return max(self.rec(s1, s2, i1 + 1, i2), self.rec(s1, s2, i1, i2 + 1))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.rec(text1, text2, 0, 0)
