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
                rs.append(r)
                P.append(r + c)
                N.append(r - c)
                s += rec(c + 1, rs, P, N)
                P.pop()
                N.pop()
                rs.pop()
            return s

        return rec(0, [], [], [])
