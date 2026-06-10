class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        def rec(c, R_arr, R, P, N):
            nonlocal res
            if c == n:
                res += 1
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