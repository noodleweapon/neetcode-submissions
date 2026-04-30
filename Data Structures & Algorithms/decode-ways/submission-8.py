class Solution:
    def numDecodings(self, s: str) -> int:
        C = 0
        def valid(n):
            if len(n) == 2 and n[0] == '0':
                return False
            return 0 < int(n) < 27

        res = 0
        def rec(i):
            nonlocal res
            if i == -1:
                res += 1
                return
            if valid(s[i]):
                rec(i - 1)
            if i > 0 and valid(s[i - 1] + s[i]):
                rec(i - 2)

        rec(len(s) - 1)
        return res