class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def generate(R):
            rows = []
            for r in range(n):
                row = ""
                for c in range(n):
                    row += "Q" if c == R[r] else "."
                rows.append(row)
            res.append(rows)

        def rec(c, R, P, N):
            if c == n:
                generate(R)
                return
            
            for r in range(n):
                if r in R:
                    continue
                pos = r - c
                neg = r + c
                if pos in P:
                    continue
                if neg in N:
                    continue
                R.append(r)
                P.append(pos)
                N.append(neg)
                rec(c + 1, R, P, N)
                R.pop()
                P.pop()
                N.pop()

        rec(0, [], [], [])

        return res