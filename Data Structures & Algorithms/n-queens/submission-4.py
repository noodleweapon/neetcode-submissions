class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def generate(R_arr):
            rows = []
            for r in range(n):
                row = ""
                for c in range(n):
                    row += "Q" if c == R_arr[r] else "."
                rows.append(row)
            res.append(rows)

        def rec(c, R_arr, R, P, N):
            if c == n:
                generate(R_arr)
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
                R_arr.append(r)
                R.add(r)
                P.add(pos)
                N.add(neg)
                rec(c + 1, R_arr, R, P, N)
                R_arr.pop()
                R.remove(r)
                P.remove(pos)
                N.remove(neg)

        rec(0, [], set(), set(), set())

        return res