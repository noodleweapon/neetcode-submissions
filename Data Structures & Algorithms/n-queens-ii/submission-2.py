class Solution:
    def totalNQueens(self, n: int) -> int:
        def rec(c, rs, P, N):
            if c == n:
                return 1
            s = 0
            for r in range(n):
                if r in rs:
                    continue
                if r + c in P:
                    continue
                if r - c in N:
                    continue
                rs.add(r)
                P.add(r + c)
                N.add(r - c)
                s += rec(c + 1, rs, P, N)
                P.remove(r + c)
                N.remove(r - c)
                rs.remove(r)
            return s

        return rec(0, set(), set(), set())
