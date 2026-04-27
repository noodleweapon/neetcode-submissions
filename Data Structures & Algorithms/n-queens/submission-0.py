class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        def gen_out(rs):
            grid = ['' for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    char = 'Q' if rs[c] == r else '.'
                    grid[r] += char
            return grid
        
        def queens_ok(rs):
            # assumes nothing is vertically / horizontally in-line
            f_slash = set()
            b_slash = set()
            for c in range(len(rs)):
                r = rs[c]
                if r - c in f_slash:
                    return False
                f_slash.add(r - c)
                if r + c in b_slash:
                    return False
                b_slash.add(r + c)
            return True

        def rec(rs):
            if len(rs) == n:
                out.append(gen_out(rs))
                return
            for r in range(n):
                if r in rs:
                    continue
                rs.append(r)
                if queens_ok(rs):
                    rec(rs)
                rs.pop()

        rec([])
        return out
        
        # free = [[False] * n for _ in range(n)]