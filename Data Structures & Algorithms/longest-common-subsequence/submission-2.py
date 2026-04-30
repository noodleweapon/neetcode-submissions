class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        def rec(i1, i2):
            if i1 >= n1 or i2 >= n2:
                return 0
            res = max(rec(i1 + 1, i2), rec(i1, i2 + 1))
            if text1[i1] == text2[i2]:
                res = 1 + max(res, rec(i1 + 1, i2 + 1))
            return res
        return rec(0, 0)