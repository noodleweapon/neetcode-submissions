class Solution:
    def totalNQueens(self, n: int) -> int:

        def attacks(rs):
            P = set()
            N = set()
            for c, r in enumerate(rs):
                pos = r + c
                neg = r - c
                if pos in P:
                    return True
                if neg in N:
                    return True
                P.add(pos)
                N.add(neg)
            return False

        def rec(i, rs):
            if i == n:
                return 1
            s = 0
            for r in range(n):
                if r in rs:
                    continue
                rs.append(r)
                if not attacks(rs):
                    s += rec(i + 1, rs)
                rs.pop()
            return s

        return rec(0, [])
